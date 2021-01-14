from django.contrib.auth.views import LogoutView
from django.urls import path
from login.views import *


urlpatterns = [

    path('login/', LoginFormView.as_view(), name = 'Login'),
    path('logout/', LogoutView.as_view(next_page='Login'), name = 'Logout'),



]