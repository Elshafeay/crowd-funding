from django.contrib.auth import get_user
from django.db.models import Sum
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods

from .forms import UserRegisterForm, UserUpdateForm
from django.contrib import messages
from django.contrib import auth
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.utils import six
from django.core.mail import EmailMessage

from django.contrib.auth.decorators import login_required
from django.conf import settings
from .models import UserModel


def register(request):
    if request.user.is_authenticated:
        redirect('home')
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            save_it = form.save(commit=False)
            save_it.is_active = False
            save_it.save()
            current_site = get_current_site(request)

            subject = 'Activate Your Crowd Funding Account'
            token = urlsafe_base64_encode(
                force_bytes(
                    save_it.pk +
                    save_it.date_joined.year +
                    save_it.date_joined.month +
                    save_it.date_joined.day
                )
            )

            activation_link = "{0}/activate/{1}".format(current_site, token)
            message = "Hello {0},\n thanks for joining Crowd Funding,\n " \
                      "click this link to activate your Account \n" \
                      "{1} \n" \
                      "thanks,".format(save_it.first_name, activation_link)

            to_list = [save_it.email, settings.EMAIL_HOST_USER]
            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                to_list, fail_silently=False
            )

            messages.success(
                request,
                'Please activate your account using '
                'the message sent to your E-mail Address'
            )
            return redirect('login')
    else:
        print(request.user)
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@require_http_methods("POST")
@login_required
def logout(request):
    auth.logout(request)
    messages.success(request, 'You have Successfully logged out!')
    return redirect('login')


def activate(request, code):
    all_users = UserModel.objects.all()
    for user in all_users:
        token = urlsafe_base64_encode(force_bytes(user.pk +
                                                  user.date_joined.year +
                                                  user.date_joined.month +
                                                  user.date_joined.day
                                                  ))
        if code == token:
            print("code", code, " ", token)
            user.is_active = 1
            user.save()

            messages.success(
                request,
                'Your account is activated, you can login now'
            )
            return redirect('login')

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
        u_profile = UserUpdateForm(request.POST, request.FILES, instance=request.user)
        if u_profile.is_valid():
            u_profile.save()
            messages.success(request, f'Your account has been has updated ')
            return redirect('profile')
    else:
        u_profile = UserUpdateForm(instance=request.user)

    context = {'u_profile': u_profile}
    return render(request, 'users/update_profile.html', context)


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
