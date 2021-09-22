from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.views.generic import View


def register(request):
    """
    Использует встроенную форму регистрации Django.
    """
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return render(request, 'users/index.html')

    context = {'form': form}
    return render(request, 'registration/register.html', context)
