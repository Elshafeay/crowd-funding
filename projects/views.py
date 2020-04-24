from django.shortcuts import render, redirect
from .models import Project, Donation
from .forms import DonateForm
from django.http import HttpResponse


# Create your views here.


def show(request, project_id):
    project = Project.objects.get(id=project_id)
    donate_form = DonateForm({'user_id': 1})
    context = {'project': project, 'donate_form': donate_form}
    return render(request, 'projects/show.html', context)


def donate(request, project_id):
    if request.method == 'POST':
        donation_form = DonateForm(request.POST)
        project = Project.objects.get(id=project_id)
        context = {'project': project, 'donate_form': donation_form}
        if donation_form.is_valid():
            donation = Donation(donation=donation_form.cleaned_data['donation'],
                                user_id=donation_form.cleaned_data['user_id'], project_id=project_id)
            donation.save()
            # project.donations.add(donation)

        return render(request, 'projects/show.html', context)
