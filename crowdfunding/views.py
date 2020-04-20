from django.shortcuts import render


def welcome(request):
	return render(request, "projects/home_page.html")