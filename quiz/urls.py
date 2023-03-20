from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name='home'),
    path('accounts/register', register, name='register'),
]
