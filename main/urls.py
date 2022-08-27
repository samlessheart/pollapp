from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home,  name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='main/login.html'), name='login' ),
    path('logout/', views.log_out, name='logout'),
    path('register/', views.register, name='register'),
    path('make_poll/', views.make_poll, name='make_poll'),
    path('profile/', views.profile, name='profile'),
    path('answer/<int:pk>/', views.answer, name='answer'),
]
