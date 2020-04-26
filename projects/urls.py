from django.urls import path
from .views import \
    show, donate, projects_list, show_all, create, \
    donate_list, show_create_project, add_comment, delete_comment, report_comment

urlpatterns = [
    path('<int:project_id>/', show, name='show_project'),
    path('<int:project_id>/donate', donate, name='donate_project'),
    path('', show_all, name='show_project'),
    path('donation/', donate_list),
    path('create/', show_create_project, name='show_create_project'),
    path('create/submit/', create, name='create_project'),
    path('self/', projects_list),
    path('<int:project_id>/add-comment', add_comment, name='add_comment'),
    path('delete-comment/', delete_comment, name='delete_comment'),
    path('report-comment/', report_comment, name='report_comment'),
]
