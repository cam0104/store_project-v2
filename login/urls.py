from django.urls import path
from login import views


urlpatterns = [

    path('', views.LoginFormView.as_view(), name = 'Login'),


]