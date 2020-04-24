from django.shortcuts import render
from .models import Project, Donation
from .forms import DonateForm,CreateForm
from django.contrib import messages


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

def show_create_project(request):
    context = { 'create_form': CreateForm}
    return render(request, 'projects/create_project.html',context)

def create(request):
    if request.method == 'POST':
        create_form = CreateForm(request.POST)
        context = {'create_form': create_form}
        if create_form.is_valid():
            project = Project(
                title=create_form.cleaned_data['title'],
                details=create_form.cleaned_data['details'],
                target=create_form.cleaned_data['target'],
                start_date=create_form.cleaned_data['start_date'],
                end_date=create_form.cleaned_data['end_date'],
                owner_id=request.user.id
            )
            project.save()
            messages.success(request, 'Form submission successful')
            return render(request, 'projects/create_project.html', context)
        else:
            return render(request, 'projects/create_project.html', context)

def projects_list(request):
    projects = Project.objects.all()
    context = {"projects": projects}
    return render(request, 'projects/project_list.html', context)


