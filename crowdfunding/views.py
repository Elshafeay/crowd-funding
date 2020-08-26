from django.shortcuts import render, render_to_response
from projects.models import Category, FeaturedProject, Project, Tag, ProjectTags
from projects.views import get_context


def welcome(request):
    highest_five_rated = Project.objects.filter(status=0).order_by('-rate')[:5]
    latest_five_projects = Project.objects.all().order_by('-created_at')[:5]
    featured_project = FeaturedProject.objects.all().order_by('-featured_at')[:5]
    featured_project = [_.project for _ in featured_project]
    latest_context = get_context(request, latest_five_projects)
    featured_context = get_context(request, featured_project)

    categories_and_projects = get_categories_have_highest_projects_number()
    first_category = categories_and_projects.get('first_category')
    categories = categories_and_projects.get('categories')
    if first_category:
        context = {
            "highest_five_rated": highest_five_rated,
            "latest_five_projects": latest_five_projects,
            "featured_project": featured_project,
            "latest_donations": latest_context.get('donations'),
            "latest_total_donations": latest_context.get('total_donations'),
            "featured_donations": featured_context.get('donations'),
            "featured_total_donations": featured_context.get('total_donations'),
            "first_category": first_category,
            "categories": categories,
        }
        return render(
            request,
            'projects/home_page.html',
            context,
        )
    else:
        return render(
            request,
            "projects/home_page.html",
            {
                "highest_five_rated": highest_five_rated,
                "featured_project": featured_project,
            }
        )


def get_categories_have_highest_projects_number():
    category_projects = {}
    categories = Category.objects.all()

    for cat in categories:
        category_projects[cat] = len(cat.project_set.all())

    category_projects = sorted(
        category_projects.items(),
        key=lambda x: x[1],
        reverse=True
    )[:5]

    if len(category_projects) > 1:
        categories = [cat[0] for cat in category_projects]
        first_category = categories[0]
        return {"first_category": first_category, "categories": categories}
    else:
        return {}


def category_project(request, cat_id):
    try:
        get_category = Category.objects.get(pk=cat_id)
        projects = get_category.project_set.all()
        context = get_context(request, projects)
        context["title"] = "All Projects Related to " + get_category.name + " category"
        context["found"] = 1
        return render(
            request,
            'projects/search_projects.html',
            context,
        )
    except Category.DoesNotExist:
        context = {
            "projects": [],
            "title": "Sorry",
            "found": -1,
        }
        return render(
            request,
            'projects/search_projects.html',
            context,
        )


def all_category(request):
    categories = Category.objects.all()
    return render(
        request,
        'projects/all_categories.html',
        {
            "categories": categories,
        },
    )


def all_tags(request):
    tags = Tag.objects.all()
    return render(
        request,
        'projects/all_tags.html',
        {
            "tags": tags,
        },
    )


def tag_projects(request, tag_id):
    try:
        tag_projects = ProjectTags.objects.filter(tag_id=tag_id)
        all_projects = Project.objects.all()

        projects = []

        for pro in all_projects:
            for tp in tag_projects:
                if pro.id == tp.project_id:
                    projects.append(pro)

        context = get_context(request, projects)
        context["title"] = "All Projects Related to " + Tag.objects.get(id=tag_id).name + " tag"
        context["found"] = 1
        return render(
            request,
            'projects/search_projects.html',
            context,
        )
    except ProjectTags.DoesNotExist:
        context = {
            "projects": [],
            "title": "Sorry",
            "found": -1,
        }
        return render(
            request,
            'projects/search_projects.html',
            context,
        )


def search(request):
    key_word = request.GET.get('Search')
    if key_word != "":
        search_by_title = Project.objects.filter(title__icontains=key_word)
        search_by_tag = ProjectTags.objects.filter(tag__name__icontains=key_word)

        projects = [_.project for _ in search_by_tag]

        for proj in search_by_title:
            projects.append(proj)

        projects = list(dict.fromkeys(projects))
        if len(projects) == 0:
            context = {
                "projects": [],
                "title": "Sorry",
                "found": -1,
            }
            return render(
                request,
                'projects/search_projects.html',
                context,
            )

        else:
            context = get_context(request, projects)
            context["title"] = "Your Search Keyword is ' "+key_word+" '"
            context["found"] = 1
            return render(
                request,
                'projects/search_projects.html',
                context,
            )

    context = {
        "projects": [],
        "title": "Sorry",
        "found": -1,
    }
    return render(
        request,
        'projects/search_projects.html',
        context,
    )


def error(request, exception):
    response = render_to_response('projects/404.html')
    response.status_code = 404
    return response
