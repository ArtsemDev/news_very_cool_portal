from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django.forms import TextInput, EmailInput, PasswordInput, CharField, ModelForm

from blog.models import Post


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username': TextInput(
                attrs={
                    'name': 'name',
                    'id': 'name',
                    'placeholder': 'Your Username'
                }
            ),
            'email': EmailInput(
                attrs={
                    'name': 'email',
                    'id': 'email',
                    'placeholder': 'Your Email'
                }
            ),
            'password1': PasswordInput(
                attrs={
                    'name': 'pass',
                    'id': 'pass',
                    'placeholder': 'Your Password'
                }
            ),
            'password2': PasswordInput(
                attrs={
                    'name': 're_pass',
                    'id': 're_pass',
                    'placeholder': 'Repeat Password'
                }
            ),
        }


class SignInForm(AuthenticationForm):
    username = UsernameField(widget=TextInput(
        attrs={
            'name': 'your_name',
            'id': 'your_name',
            'placeholder': 'Your Username'
        }
    )
    )
    password = CharField(
        label="Password",
        strip=False,
        widget=PasswordInput(attrs={
            'name': 'your_pass',
            'id': 'your_pass',
            'placeholder': 'Your Password'
        }),
    )


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'subtitle', 'text', 'image', 'is_published')
