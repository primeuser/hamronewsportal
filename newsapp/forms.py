from django import forms
from django.forms import Select
from .models import *


class AdminRegistrationForm(forms.ModelForm):
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Choose Username',
    }),)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter Password',
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Confirm Password',
    }))

    class Meta:
        model = Admin
        fields = ['username', 'password1', 'password2',
                  'name', 'phone', 'address', 'email', 'about', 'image']
        widgets = {

            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Name',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'data-validation': 'required',
                'pattern': '[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,3}$',
                'placeholder': 'Enter your email',
            }),
            'phone': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Phone Number',
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Address',
            }),

        }

    def clean(self):
        cleaned_data = super(AdminRegistrationForm, self).clean()
        username = cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("username already exists")
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        if password1 != password2:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )


class EditorRegistrationForm(forms.ModelForm):
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Choose Username',
    }),)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter Password',
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Confirm Password',
    }))

    class Meta:
        model = Editor
        fields = ['username', 'password1', 'password2',
                  'name', 'phone', 'address', 'email', 'about', 'image']
        widgets = {

            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Name',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'data-validation': 'required',
                'pattern': '[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,3}$',
                'placeholder': 'Enter your email',
            }),
            'phone': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Phone Number',
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Address',
            }),

        }

    def clean(self):
        cleaned_data = super(EditorRegistrationForm, self).clean()
        username = cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("username already exists")
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        if password1 != password2:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )


class SubscriberRegistrationForm(forms.ModelForm):
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Choose Username',
    }),)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter Password',
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Confirm Password',
    }))

    class Meta:
        model = Subscriber
        fields = ['username', 'password1', 'password2',
                  'name', 'phone', 'address', 'email', 'image']
        widgets = {

            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Name',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'data-validation': 'required',
                'pattern': '[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,3}$',
                'placeholder': 'Enter your email',
            }),
            'phone': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Phone Number',
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Address',
            }),

        }

    def clean(self):
        cleaned_data = super(SubscriberRegistrationForm, self).clean()
        username = cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("username already exists")
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        if password1 != password2:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter Username',
    }),)
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter Password',
    }))


class PasswordChangeForm(forms.Form):
    new_password = forms.CharField(widget=forms.PasswordInput)
    confirm_new_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super(PasswordChangeForm, self).clean()
        new_password = cleaned_data.get("new_password")
        confirm_new_password = cleaned_data.get("confirm_new_password")


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'image', 'author', 'category']

        widgets = {
            'description': forms.Textarea(attrs={
                'placeholder': 'Write Something...',
                'rows': '5',
                'cols': '50',
                'class': 'form-control',
            }),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']

        widgets = {
            'comment': forms.Textarea(attrs={
                'placeholder': 'Write Something...',
                'rows': '5',
                'cols': '50',
                'class': 'form-control',
            }),
        }
