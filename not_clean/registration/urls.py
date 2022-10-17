from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import SignUpView, SignInView, AccountView


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signin/', SignInView.as_view(), name='signin'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('accounts/profile/', AccountView.as_view(), name='profile')
]
