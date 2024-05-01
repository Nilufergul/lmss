from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # user = User()
            # user.username = form.cleaned_data['username'].lower()

            user.save()

            # Redirect to login page or another URL upon successful registration
            return redirect('create_lesson')
    else:
        form = UserCreationForm()

    return render(request, 'register/register.html', {'form': form})
