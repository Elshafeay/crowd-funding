from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from crowdfunding import settings
from .views import welcome, category_project, all_category
from django.contrib.auth import views as auth_views
from users.views import register, logout, profile,update_profile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', welcome, name='home'),
    path('category/<int:cat_id>', category_project),
    path('categories/', all_category),
    path('profile/', profile, name='profile'),
    path('update_profile/', update_profile, name='update_profile'),
    path('register/', register, name='register'),
    path('login/',
         auth_views.LoginView.as_view(template_name='users/login.html'),
         name='login'),
    path('logout/', logout, name='logout'),
    path('projects/', include('projects.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'crowdfunding.views.error'
