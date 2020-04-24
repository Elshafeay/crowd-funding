from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # first_name = form.cleaned_data.get('first_name')
            # last_name = form.cleaned_data.get('last_name')

            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        print (request.user)
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
