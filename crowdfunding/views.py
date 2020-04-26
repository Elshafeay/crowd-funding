from django.shortcuts import render
from projects.models import Category, FeaturedProject, Project
from django.shortcuts import get_object_or_404
from collections import OrderedDict

# Homepage should contains the following:
# - *A slider to show the highest five rated running projects to encourage users to donate
# - *List of the latest 5 projects
# - *List of latest 5 featured projects (which are selected by the admin)
# - *A list of the categories. User can open each category to view its projects
# - Search bar that enables users to search projects by title or tag


def welcome(request):
    highest_five_rated = Project.objects.filter(status=0).order_by('rate')[0:5]
    latest_five_projects = Project.objects.all().order_by('created_at')[0:5]
    featured_project = FeaturedProject.objects.all().order_by('-featured_at')[0:5]
    categories_and_projects = get_categories_have_highest_projects_number()
    first_category = categories_and_projects.get('first_category')
    categories = categories_and_projects.get('categories')
    print("first_category", first_category)
    print("categories", categories)
    if first_category:
        return render(request, 'projects/home_page.html', {"highest_five_rated": highest_five_rated,
                                                           "latest_five_projects": latest_five_projects,
                                                           "featured_project": featured_project,
                                                           "first_category": first_category,
                                                           "categories": categories,
                                                           })
    else:
        return render(request, "projects/home_page.html", {"highest_five_rated": highest_five_rated,
                                                           "highest_five_rated": highest_five_rated,
                                                           "featured_project": featured_project,
                                                           })


def get_categories_have_highest_projects_number():
    category_projects = {}
    categories = Category.objects.all()

    for cat in categories:
        category_projects[cat.id] = len(cat.project_set.all())

    category_projects = OrderedDict(sorted(category_projects.items(), key=lambda x: x[1]))

    if len(category_projects) > 1:
        new_categories_list_id = []
        for cat2 in categories:
            for cat1 in category_projects:
                if cat1 == cat2.id:
                    new_categories_list_id.append(cat1)
        new_categories_list_id = new_categories_list_id[0:5]
        new_categories_list = Category.objects.filter(pk__in=new_categories_list_id[0:5])
        first_category = new_categories_list[0]
        categories = new_categories_list[1:]
        return {"first_category": first_category, "categories": categories}
    else:
        return {}
