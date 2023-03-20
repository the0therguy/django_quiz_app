from django.shortcuts import render

from .forms import *


# Create your views here.

def home(request):
    return render(request, 'home.html')


def register(request):
    form = RegisterUserForm
    message = ''
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            message = 'Registration Successfully'
    return render(request, 'registration/register.html', {'form': form, 'msg': message})
