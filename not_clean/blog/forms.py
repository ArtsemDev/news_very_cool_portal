from django.forms import ModelForm, TextInput, Textarea, EmailInput

from .models import Contact


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'message')
        widgets = {
            'name': TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'name',
                    'type': 'text',
                    'placeholder': 'Кто по масти?',
                    'required': True
                }
            ),
            'email': EmailInput(
                attrs={
                    'class': 'form-control',
                    'id': 'email',
                    'type': 'email',
                    'placeholder': 'Мыло',
                    'required': True
                }
            ),
            'message': Textarea(
                attrs={
                    'class': 'form-control',
                    'id': 'message',
                    'placeholder': 'Малява',
                    'style': 'height: 12rem',
                    'required': True
                }
            )
        }
