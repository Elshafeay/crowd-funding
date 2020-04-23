from django.shortcuts import render
from .models import Project
from django.http import HttpResponse


# Create your views here.


def show(request, project_id):
    project = Project.objects.get(id=project_id)
    context = {"project": project}
    return render(request, 'projects/show.html', context)
