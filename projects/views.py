from django.contrib.auth import get_user
from django.shortcuts import render
from .models import Project, Donation,Category
from .forms import DonateForm,CreateForm
from django.contrib import messages
from django.shortcuts import redirect


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

categories = Category.objects.all()

def show_create_project(request):
    context = { 'create_form': CreateForm , 'categories' : categories}
    return render(request, 'projects/create_project.html',context)

def create(request):
    if request.method == 'POST':
        create_form = CreateForm(request.POST,request.FILES)
        context = {'create_form': create_form,'categories' : categories}
        if create_form.is_valid():
            project = Project(
                title=create_form.cleaned_data['title'],
                details=create_form.cleaned_data['details'],
                target=create_form.cleaned_data['target'],
                cover = request.FILES['cover'],
                category_id = request.POST['categ'],
                start_date=create_form.cleaned_data['start_date'],
                end_date=create_form.cleaned_data['end_date'],
                owner_id=request.user.id
            )
            project.save()
            messages.success(request, 'Project Created Successfully')
            return redirect('/projects/create')
        else:
            return render(request, 'projects/create_project.html', context)

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


