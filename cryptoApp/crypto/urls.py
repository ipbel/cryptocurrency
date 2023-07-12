from django.urls import path

from crypto import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.SignupPage, name='signup'),
    path('login/', views.LoginPage, name='login')
]
