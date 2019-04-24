from django.shortcuts import render, redirect
from django.views.generic import *
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from .models import *
from .forms import *
from django.urls import reverse, reverse_lazy
from django.views import generic
# Create your views here.


class BaseMixin(object):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['postlist'] = Post.objects.all()
        context['postform'] = PostForm
        # context['commentform'] = CommentForm
        return context


class AdminMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('cmsapp:login'))
        else:
            user_group = []
            for group in request.user.groups.all():
                user_group.append(group.name)
            if user_group != ['Admin']:
                return HttpResponseRedirect(reverse_lazy('cmsapp:login'))
        return super(AdminMixin, self).dispatch(request, *args, **kwargs)


class EditorMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('cmsapp:login'))
        else:
            user_group = []
            for group in request.user.groups.all():
                user_group.append(group.name)
            if user_group != ['Editor']:
                return HttpResponseRedirect(reverse_lazy('cmsapp:login'))
        return super(EditorMixin, self).dispatch(request, *args, **kwargs)


class HomeView(TemplateView):
    template_name = 'home.html'


class ContactView(TemplateView):
    template_name = 'contact.html'


class AdminPanelView(TemplateView):
    template_name = 'adminbase.html'


class EditorPanelView(TemplateView):
    template_name = 'editorbase.html'


class AdminRegistrationView(AdminMixin, CreateView):
    template_name = 'admincreate.html'
    form_class = AdminRegistrationForm
    success_url = reverse_lazy('newsapp:adminpanel')

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password2']
        user = User.objects.create_user(username, "", password)
        group = Group.objects.get(name="Admin")
        group.user_set.add(user)
        form.instance.user = user

        return super().form_valid(form)


class EditorRegistrationView(CreateView):
    template_name = 'editorcreate.html'
    form_class = EditorRegistrationForm
    success_url = reverse_lazy('newsapp:adminpanel')

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password2']
        user = User.objects.create_user(username, "", password)
        group = Group.objects.get(name="Editor")
        group.user_set.add(user)
        form.instance.user = user

        return super().form_valid(form)


class SubscriberRegistrationView(CreateView):
    template_name = "Subscribercreate.html"
    form_class = SubscriberRegistrationForm
    success_url = reverse_lazy("newsapp:home")
    success_message = 'You have been Subscribed now you can comment in our posts.'

    def form_valid(self, form):
        subject = 'Registration Confirmation'
        message = 'Thank you for registering.'
        email_from = 'settings.EMAIL_HOST_USER'
        recipient_list = [form.instance.email]
        send_mail(subject, message, email_from,
                  recipient_list, fail_silently=False)
        return super().form_valid(form)


class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request, user)
            if Admin.objects.filter(user=user).exists():
                return HttpResponseRedirect(reverse_lazy('newsapp:adminpanel'))
            elif Editor.objects.filter(user=user).exists():
                return HttpResponseRedirect(reverse_lazy('newsapp:editorpanel'))
        else:
            return render(self.request, self.template_name, {
                'form': form,
                'errors': "Please correct username or password "
            })
        return super().form_valid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('newsapp:home')


class PostCreateView(BaseMixin, CreateView):
    template_name = 'postcreate.html'
    form_class = PostForm

    def form_valid(self, form):
        user = self.request.user
        form.instance.post_by = user
        self.post_id = form.save().id
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("newsapp:postlist")


class PostUpdateView(UpdateView):
    template_name = 'postcreate.html'
    form_class = PostForm
    model = Post
    success_url = "/post/list"


class PostDeleteView(DeleteView):
    template_name = 'postlist.html'
    model = Post
    success_url = "/post/list"


class PostListView(BaseMixin, generic.ListView):
    template_name = 'postlist.html'
    model = Post
    context_object_name = 'postlist'


class PostDetailView(DetailView):
    template_name = 'postdetail.html'
    model = Post
    context_object_name = 'postdetail'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['commentform'] = CommentForm
        return context


class CommentCreateView(BaseMixin, CreateView):
    template_name = 'newspost.html'
    form_class = CommentForm
    success_url = '/post/list/'

    def form_valid(self, form):
        post_id = self.kwargs['pk']
        post = Post.objects.get(id=post_id)
        form.instance.post = post
        form.instance.comment_by = self.request.user

        return super().form_valid(form)



class CommentUpdateView(UpdateView):
    template_name = 'newspost.html'
    form_class = CommentForm
    model = Comment
    success_url = "post/list/"


class CommentDeleteView(DeleteView):
    template_name = 'newspost.html'
    model = Comment
    success_url = "post/list/"


class SearchResultView(TemplateView):
    template_name = 'searchresult.html'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q')
        if query:
            lookup = Q(name__icontains=query)
            postlist = Post.objects.filter(lookup)
            context['postlist'] = postlist
            return context
