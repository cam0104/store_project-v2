from django.urls import path
from home_page import views


urlpatterns = [

    path('', views.IndexView.as_view(), name = 'Index'),


]