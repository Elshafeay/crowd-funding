from django.urls import path
from .views import show, donate, projects_list, show_all, create, donate_list, show_create_project

urlpatterns = [
    path('<int:project_id>/', show, name='show_project'),
    path('<int:project_id>/donate', donate, name='donate_project'),
    path('', show_all, name='show_project'),
    path('donation/', donate_list),
    path('create/', show_create_project, name='show_create_project'),
    path('create/submit/', create, name='create_project'),
    path('self/', projects_list)
]
