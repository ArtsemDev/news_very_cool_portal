from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.views.generic import CreateView
from django.views import View

from .forms import SignUpForm, SignInForm, PostForm
from blog.models import Post


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('signin')
    template_name = 'registration/signup.html'


class SignInView(LoginView):
    form_class = SignInForm
    template_name = 'registration/signin.html'


class AccountView(LoginRequiredMixin, View):
    template_name = 'registration/profile.html'
    login_url = '/signin/'

    def get_queryset(self):
        return User.objects.filter(username=self.request.user)[0]

    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, self.template_name, {
            'user': self.get_queryset(),
            'form': PostForm()
        })

    def post(self, request: HttpRequest) -> HttpResponse:

        form = Post(
            title=request.POST.get('title'),
            subtitle=request.POST.get('subtitle'),
            text=request.POST.get('text'),
            image=request.POST.get('image'),
            author=request.user,
            is_published=True if request.POST.get('is_published') == 'on' else False,
            slug=slugify(request.POST.get('title') + request.POST.get('subtitle'))
        )
        form.save()
        return render(request, self.template_name, {
            'user': self.get_queryset(),
            'form': PostForm()
        })
