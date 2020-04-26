from django.contrib.auth import get_user
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_http_methods

from .models import Project, Donation, Category, Comment, CommentReports
from .forms import DonateForm, CreateForm
from django.contrib import messages
from django.shortcuts import redirect


def show(request, project_id):
    project = Project.objects.get(id=project_id)
    donate_form = DonateForm({'user_id': 1})
    comments = project.comment_set.all().order_by('-created_at')
    reported_comments = [
        report.comment for report in get_user(request).commentreports_set.all()
    ]
    context = {
        'project': project,
        'donate_form': donate_form,
        'comments': comments,
        'reported_comments': reported_comments
    }
    return render(request, 'projects/show.html', context)


@require_http_methods("POST")
def add_comment(request, project_id):
    new_comment = request.POST.get('comment')
    current_user = get_user(request)
    current_user.comment_set.create(
        project=get_object_or_404(Project, pk=project_id),
        comment=new_comment)
    return redirect('show_project', project_id)


@require_http_methods("POST")
def delete_comment(request):
    comment = get_object_or_404(Comment, pk=request.POST.get('comment_id'))
    project_id = comment.project.id
    comment.delete()
    return redirect('show_project', project_id)


@require_http_methods("POST")
def report_comment(request):
    comment = get_object_or_404(Comment, pk=request.POST.get('comment_id'))
    CommentReports.objects.create(
        comment=comment,
        user=get_user(request),
    )
    return redirect('show_project', comment.project.id)


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
    all_projects = Project.objects.all()
    categories = Category.objects.all()
    context = {"categories": categories , "all_projects": all_projects}
    return render(request, "projects/all_projects.html", context)


def show_create_project(request):
    categories = Category.objects.all()
    context = {'create_form': CreateForm, 'categories': categories}
    return render(request, 'projects/create_project.html', context)


def create(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        create_form = CreateForm(request.POST, request.FILES)
        context = {'create_form': create_form, 'categories': categories}
        if create_form.is_valid():
            project = Project(
                title=create_form.cleaned_data['title'],
                details=create_form.cleaned_data['details'],
                target=create_form.cleaned_data['target'],
                cover=request.FILES['cover'],
                category_id=request.POST['categ'],
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


def saved_projects(request):
    owner = get_user(request)
    saved_projects = owner.savedproject_set.all()
    context = {"saved_projects": saved_projects}
    return render(request, 'projects/saved_projects.html', context)
