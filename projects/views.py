import json

from django.contrib.auth import get_user
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_http_methods

from .models import \
    Project, Donation, Category, Comment, CommentReports, ProjectImages
from .forms import DonateForm, CreateForm
from django.contrib import messages
from django.shortcuts import redirect


@login_required()
def show(request, project_id):
    project = get_object_or_404(Project, id=project_id)

    is_project_canceled = project.status == -1 or False

    if is_project_canceled and project.owner_id != request.user.id:
        raise Http404("project was canceled")

    comments = project.comment_set.all().order_by('-created_at')
    reported_comments = [
        _.comment for _ in get_user(request).commentreports_set.all()
    ]
    related_projects = project.category.project_set.all()[:10]
    liked = get_user(request).review_set.filter(liked=True)
    favourites = [_.project for _ in liked]
    is_user_reported = project.review_set.filter(user_id=request.user.id)
    is_project_saved = project.savedproject_set.filter(user_id=request.user.id)
    review = get_user(request).review_set.filter(project_id=project_id).first()

    is_rated = False
    if review and review.rate:
        is_rated = True

    donation_form = DonateForm()

    if request.method == 'POST':
        donation_form = DonateForm(request.POST or None)
        if donation_form.is_valid():
            project.donation_set.create(
                user=request.user,
                donation=donation_form.cleaned_data['donation']
            )
            messages.success(request, "Donation Added Successfully")
            return redirect('show_project', project_id)

    context = {
        'project': project,
        'comments': comments,
        'favourites': favourites,
        'donation_form': donation_form,
        's_user_reported': is_user_reported,
        'is_project_saved': is_project_saved,
        'related_projects': related_projects,
        'reported_comments': reported_comments,
        'is_project_canceled': is_project_canceled,
        'is_rated': is_rated,
    }
    return render(request, 'projects/show.html', context)


@require_http_methods("POST")
def add_comment(request, project_id):
    new_comment = request.POST.get('comment')
    current_user = get_user(request)
    current_user.comment_set.create(
        project_id=project_id,
        comment=new_comment)
    return redirect('show_project', project_id)


@require_http_methods("POST")
def add_reply(request):
    comment = get_object_or_404(Comment, pk=request.POST.get('comment_id'))
    reply = request.POST.get('reply')
    current_user = get_user(request)
    current_user.reply_set.create(
        reply=reply,
        comment_id=comment
    )
    return redirect('show_project', comment.project.id)


@require_http_methods("POST")
def delete_comment(request):
    comment = get_object_or_404(Comment, pk=request.POST.get('comment_id'))
    project_id = comment.project_id
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


@require_http_methods("POST")
def change_favourites(request):
    project_id = request.POST.get('project')
    review = get_user(request).review_set.filter(
        project_id=project_id
    )[0]

    if review:
        review.liked = not review.liked
        review.save()
    else:
        review = get_user(request).review_set.create(
            project_id=project_id,
            liked=True
        )

    if review.liked:
        message = "You have Successfully added" \
                  " this project to your favourites"
    else:
        message = "You have Successfully deleted" \
                  " this project from your favourites"

    return HttpResponse(message)


@require_http_methods("POST")
def add_rate(request):
    project_id = request.POST.get('project')
    review = get_user(request).review_set.filter(
        project_i=project_id
    ).get_or_create()

    review.rate = int(request.POST.get('project'))
    review.save()
    message = "Your rate has been added successfully"
    return HttpResponse(message)


@require_http_methods("POST")
def report(request, project_id):
    get_user(request).review_set.get_or_create(
        reported=True,
        project_id=project_id
    )
    messages.success(request, "Report Added Successfully")
    return redirect('show_project', project_id)


@require_http_methods("POST")
def save(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    if project.savedproject_set.get_or_create(user_id=request.user.id)[1]:
        messages.success(request, "Project Saved Successfully")
    else:
        project.savedproject_set.get(user_id=request.user.id).delete()
        messages.success(
            request,
            "Project Removed From Your Saved Successfully"
        )

    return redirect('show_project', project_id)


@require_http_methods("POST")
def cancel(request, project_id):
    try:
        Project.objects.filter(id=project_id).update(status=-1)

    except Project.DoesNotExist:
        raise Http404("project not found")

    return redirect('show_project', project_id)


def show_all(request):
    all_projects = Project.objects.all()
    categories = Category.objects.all()
    context = {"categories": categories, "all_projects": all_projects}
    return render(request, "projects/all_projects.html", context)


def show_create_project(request):
    categories = Category.objects.all()
    context = {'create_form': CreateForm, 'categories': categories}
    return render(request, 'projects/create_project.html', context)


def create(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        create_form = CreateForm(request.POST, request.FILES)
        project_images = request.FILES.getlist('images')
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
            for image in project_images:
                photo = ProjectImages(project=project, image=image)
                photo.save()
            messages.success(request, 'Project Created Successfully')
            return redirect('show_project', project.id)
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
    my_saved_projects = owner.savedproject_set.all()
    context = {"saved_projects": my_saved_projects}
    return render(request, 'projects/saved_projects.html', context)
