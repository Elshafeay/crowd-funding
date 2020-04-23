from django.urls import path
from .views import show

urlpatterns = [
    path('<int:project_id>', show, name="show_book"),
]
