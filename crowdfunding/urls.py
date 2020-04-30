from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from crowdfunding import settings
from .views import welcome, category_project, all_category, all_tags, tag_projects
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from users.views import register, logout, activate, profile, update_profile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', welcome, name='home'),
    path('category/<int:cat_id>', category_project),
    path('categories/', all_category),
    path('tag/<int:tag_id>', tag_projects, name='show_tag'),
    path('tags/', all_tags),
    path('profile/', profile, name='profile'),
    path('update_profile/', update_profile, name='update_profile'),
    path('register/', register, name='register'),
    path('login/',
         auth_views.LoginView.as_view(template_name='users/login.html'),
         name='login'),
    path('logout/', logout, name='logout'),
    path('activate/<str:code>', activate, name='activate'),
    path('projects/', include('projects.urls')),
    path('users/', include('users.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'crowdfunding.views.error'
