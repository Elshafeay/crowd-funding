from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from crowdfunding import settings
from .views import welcome, logout
from django.contrib.auth import views as auth_views
from users.views import register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', welcome, name='home'),
    path('logout', logout, name='logout'),
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('projects/', include('projects.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
