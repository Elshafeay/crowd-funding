from django.urls import path
from .views import show_user_profile

urlpatterns = [
    path('<int:user_id>/', show_user_profile, name='show_user_profile'),
]
