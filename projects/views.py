from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import DonateForm, CreateForm
from .models import Project
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404


def show(request, project_id):
    project = get_object_or_404(Project, id=project_id)

    is_project_canceled = False
    if project.status == -1:
        is_project_canceled = True

    if is_project_canceled and project.owner_id != request.user.id:
        raise Http404("project was canceled")

    is_user_reported = project.review_set.filter(user_id=request.user.id)
    is_project_saved = project.savedproject_set.filter(user_id=request.user.id)

    context = {}
    if request.method == 'GET':
        donation_form = DonateForm()
        context = {'project': project, 'donation_form': donation_form, "is_user_reported": is_user_reported,
                   "is_project_saved": is_project_saved, 'is_project_canceled': is_project_canceled}

    elif request.method == 'POST':
        donation_form = DonateForm(request.POST or None)
        if donation_form.is_valid():
            project.donation_set.create(user_id=request.user.id, donation=donation_form.cleaned_data['donation'])
            messages.success(request, "Donation Added Successfully")
            return redirect('show_project', project_id)
        else:
            context = {'project': project, 'donation_form': donation_form, "is_user_reported": is_user_reported,
                       "is_project_saved": is_project_saved, 'is_project_canceled': is_project_canceled}
    return render(request, 'projects/show.html', context)


def report(request, project_id):
    project = get_object_or_404(Project, user_id=request.user.id)

    project.review_set.get_or_create(comment=False, liked=False, reported=True,
                                     user_id=request.user.id)
    messages.success(request, "Report Added Successfully")
    return redirect('show_project', project_id)


def save(request, project_id):
    # project = get_object_or_404(Project, user_id=request.user.id)
    project = Project.objects.get(owner_id=request.user.id)
    if project.savedproject_set.get_or_create(user_id=request.user.id)[1]:
        messages.success(request, "Project Saved Successfully")

    else:
        project.savedproject_set.get(user_id=request.user.id).delete()
        messages.success(request, "Project Removed From Your Saved Successfully")

    return redirect('show_project', project_id)


def cancel(request, project_id):
    try:
        Project.objects.filter(id=project_id).update(status=-1)

    except Project.DoesNotExist:
        raise Http404("project not found")

    return redirect('show_project', project_id)


def show_all(request):
    return render(request, 'projects/all_projects.html')


def show_create_project(request):
    context = {'create_form': CreateForm}
    return render(request, 'projects/create_project.html', context)


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
