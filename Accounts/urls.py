from django.urls import path
from Accounts.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [

path('index/', index, name='index'),
path('login', login_request, name='login'),
path('register/', register, name='register'),
path('logout/', LogoutView.as_view(), name='logout'),



]