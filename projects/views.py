from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Project, Donation
from .forms import DonateForm
from django.http import HttpResponse, HttpResponseRedirect
from .forms import DonateForm,CreateForm
from django.contrib import messages


def show(request, project_id):
    project = Project.objects.get(id=project_id)
    context = {}
    if request.method == 'GET':
        form = DonateForm()
        context = {'project': project, 'form': form}

    elif request.method == 'POST':
        form = DonateForm(request.POST or None)
        if form.is_valid():
            message = "Donation Added Successfully"
            project.donation_set.create(user_id=form.cleaned_data['user_id'], donation=form.cleaned_data['donation'])
            messages.success(request, message)
            return redirect('show_project', project_id)
        else:
            context = {'project': project, 'form': form}
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
