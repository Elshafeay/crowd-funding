from django.urls import path
from .views import show, donate, projects_list

urlpatterns = [
    path('<int:project_id>', show, name='show_project'),
    path('<int:project_id>/donate', donate, name='donate_project'),
    path('', projects_list)
]
