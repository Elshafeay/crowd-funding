from django.contrib.auth import get_user
from django.db.models import Sum
from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserRegisterForm, UserUpdateForm
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.decorators import login_required

from .models import UserModel


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
    total_donations = get_user(request).donation_set.aggregate(Sum('donation'))
    total_donations = total_donations.get('donation__sum')
    return render(
        request,
        'users/profile.html',
        {'total_donations': total_donations}
    )


@login_required
def update_profile(request):
    if request.method == 'POST':
        u_profile=UserUpdateForm(request.POST, request.FILES, instance=request.user)
        if u_profile.is_valid():
            u_profile.save() 
            messages.success(request, f'Your account has been has updated ')
            return redirect('profile')    
    else :
        u_profile=UserUpdateForm(instance=request.user)  
    
    context={'u_profile': u_profile}  
    return render(request,'users/update_profile.html',context)


@login_required
def show_user_profile(request, user_id):
    user = get_object_or_404(UserModel, pk=user_id)
    total_donations = user.donation_set.aggregate(Sum('donation'))
    total_donations = total_donations.get('donation__sum')
    context = {'total_donations': total_donations, 'user': user}
    return render(
        request,
        'users/profile.html',
        context
    )
