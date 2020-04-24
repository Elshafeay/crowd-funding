from django.urls import path
from .views import show, donate, projects_list,show_all,create_project

urlpatterns = [
    path('<int:project_id>', show, name='show_project'),
    path('<int:project_id>/donate', donate, name='donate_project'),
    path('', show_all, name='show_project'),
    path('create', create_project, name='create_project'),
    path('self', projects_list)
]

