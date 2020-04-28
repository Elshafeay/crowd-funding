from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Your account has been created Successfully!'
                ' You can log in now'
            )
            return redirect('login')
    else:
        print(request.user)
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


def logout(request):
    auth.logout(request)
    messages.success(request, 'You have Successfully logged out!')
    return redirect('login')


@login_required
def profile(request):
    return render(request,'users/profile.html')
