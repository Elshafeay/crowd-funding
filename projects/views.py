from django.contrib.auth import get_user
from django.shortcuts import render
from .models import Project, Donation
from .forms import DonateForm


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
            donation = Donation(
                donation=donation_form.cleaned_data['donation'],
                user_id=donation_form.cleaned_data['user_id'],
                project_id=project_id
            )
            donation.save()
            # project.donations.add(donation)
            return render(request, 'projects/show.html', context)
        else:
            return render(request, 'projects/show.html', context)

def show_all(request):
    return render(request, 'projects/all_projects.html')

def create_project(request):
    return render(request, 'projects/create_project.html')

def projects_list(request):
    owner = get_user(request)
    projects = owner.project_set.all()
    context = {"projects": projects}
    return render(request, 'projects/project_list.html', context)

def donate_list(request):
    owner = get_user(request)
    donations = owner.donation_set.all()
    context = {"donations": donations}
    return render(request, 'projects/donation_list.html', context)


