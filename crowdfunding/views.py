from django.shortcuts import render
from projects.models import Category
# Homepage should contains the following:
# - A slider to show the highest five rated running projects to encourage users to donate
# - List of the latest 5 projects
# - List of latest 5 featured projects (which are selected by the admin)
# - A list of the categories. User can open each category to view its projects
# - Search bar that enables users to search projects by title or tag


def welcome(request):
	gcategories = getCategoriesAndProjects()
	firstCategory =gcategories['firstCategory']
	categories =gcategories['categories']
	if(firstCategory):
		return render(request, "projects/home_page.html", {"firstCategory": firstCategory, "categories": categories, "firstCategoryProjects":gcategories['firstCategoryProjects']})
	else:
		return render(request, "projects/home_page.html", {})


def getCategoriesAndProjects():
	categories = Category.objects.all()
	if len(categories) > 1:
		firstCategory = categories[0]
		firstCategoryProjects = categories[0].project_set.all()
		categories = categories.exclude(id=firstCategory.id)
		return {"firstCategory": firstCategory, "categories": categories, "firstCategoryProjects":firstCategoryProjects}
	else:
		return {}
# print(categories)


