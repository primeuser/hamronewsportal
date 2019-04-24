from django.urls import path, include
from .views import *
from .models import *

app_name = 'newsapp'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('adminpanel/', AdminPanelView.as_view(), name='adminpanel'),
    path('editorpanel/', EditorPanelView.as_view(), name='editorpanel'),
    path('admin/registration/', AdminRegistrationView.as_view(),
         name='adminregistration'),
    path('editor/registration/', EditorRegistrationView.as_view(),
         name='editorregistration'),
    path('subscriber/registration/', SubscriberRegistrationView.as_view(),
         name='subscriberregistration'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('post/create/', PostCreateView.as_view(), name='postcreate'),
    path('post/<int:pk>/detail/', PostDetailView.as_view(), name='postdetail'),
    path('post/list/', PostListView.as_view(),
         name='postlist'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='postupdate'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='postdelete'),
    path('post/<int:pk>/comment/create/',
         CommentCreateView.as_view(), name='commentcreate'),
    path('post/<int:pk>/comment/update',
         CommentUpdateView.as_view(), name='commentupdate'),
    path('post/<int:pk>/comment/delete',
         CommentDeleteView.as_view(), name='commentdelete'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('search/result/', SearchResultView.as_view(), name='searchresult')


]
