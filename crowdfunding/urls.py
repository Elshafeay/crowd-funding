from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from crowdfunding import settings
from projects.views import donate_list, saved_projects, projects_list
from .views import welcome, category_project, all_category, all_tags, tag_projects
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from users.views import register, logout, activate, profile, update_profile, delete_my_account


urlpatterns = [
    path('admin/', admin.site.urls),
    path('projects/', include('projects.urls')),
    path('users/', include('users.urls')),
    path('users/', include('accounts.urls')),
    path('', welcome, name='home'),
    path('category/<int:cat_id>', category_project, name='show_category'),
    path('categories/', all_category, name='show_all_categories'),
    path('tag/<int:tag_id>', tag_projects, name='show_tag'),
    path('tags/', all_tags, name='show_all_tag'),
    path('profile/', profile, name='profile'),
    path('update_profile/', update_profile, name='update_profile'),
    path('register/', register, name='register'),
    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='users/login.html',
            redirect_authenticated_user=True
        ),
        name='login'
    ),
    path('logout/', logout, name='logout'),
    path('activate/<str:code>', activate, name='activate'),
    path('my-donations/', donate_list, name='show_donations'),
    path('saved-projects/', saved_projects, name='saved_projects'),
    path('my-projects/', projects_list, name='my_projects'),
    path('delete-my-account/', delete_my_account, name='delete-my-account'),
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'crowdfunding.views.error'
