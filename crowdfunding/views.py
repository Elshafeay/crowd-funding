from django.shortcuts import render, render_to_response
from projects.models import Category, FeaturedProject, Project, Tag, ProjectTags


# Homepage should contains the following:
# - *A slider to show the highest five rated running projects to encourage users to donate
# - *List of the latest 5 projects
# - *List of latest 5 featured projects (which are selected by the admin)
# - *A list of the categories. User can open each category to view its projects
# - Search bar that enables users to search projects by title or tag


def welcome(request):
    if request.GET.get('Search'):
        projects = search(request)
        context = {
            "projects": projects,
            "title": "Your Search Key Word is ' " + request.GET['Search'] + " ' ",
            "found": 1
        }
        return render(
            request,
            'projects/search_projects.html',
            context,
        )

    else:
        highest_five_rated = Project.objects.filter(status=0).order_by('-rate')[:5]
        latest_five_projects = Project.objects.all().order_by('-created_at')[:5]
        featured_project = FeaturedProject.objects.all().order_by('-featured_at')[:5]
        categories_and_projects = get_categories_have_highest_projects_number()
        first_category = categories_and_projects.get('first_category')
        categories = categories_and_projects.get('categories')
        print("first_category", first_category)
        print("categories", categories)
        if first_category:
            context = {
                "highest_five_rated": highest_five_rated,
                "latest_five_projects": latest_five_projects,
                "featured_project": featured_project,
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
    # category_projects = OrderedDict(sorted(category_projects.items(),
    # key=lambda x: x[1],
    # reverse=True))

    category_projects = sorted(
        category_projects.items(),
        key=lambda x: x[1],
        reverse=True
    )[:5]
    print("category_projects2", category_projects)

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
        context = {
            "projects": projects,
            "title": "All Projects Related to " + get_category.name + " category",
            "found": 1
        }
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

        context = {
            "projects": projects,
            "title": "All Projects Related to " + Tag.objects.get(id=tag_id).name + " tag",
            "found": 1
        }
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
    key_word = request.GET['Search']

    projects = []
    search_by_title = Project.objects.filter(title__icontains=key_word)

    search_by_tage = Tag.objects.filter(name__icontains=key_word)
    all_projects = Project.objects.all()

    for tag in search_by_tage:
        for pro in ProjectTags.objects.filter(tag_id=tag.id):
            for proj in all_projects:
                if proj.id == pro.project_id:
                    projects.append(proj)
    for proj in search_by_title:
        projects.append(proj)

    projects = list(dict.fromkeys(projects))

    return projects


def error(request, exception):
    response = render_to_response('projects/404.html')
    response.status_code = 404
    return response
