from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='users-register'),
    path('profile/', views.profile, name='users-profile'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='users-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='users-logout')
]
