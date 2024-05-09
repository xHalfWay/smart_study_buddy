"""
URL configuration for smart_study_buddy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('profile/', views.profile_view, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/change-password/', views.change_password, name='change_password'),  
    path('logout/', views.logout_view, name='logout'),
    path('task_creation/', views.task_creation, name='task_creation'),
    path('create_find_pair_task/', views.create_find_pair_task, name='create_find_pair_task'),
    path('task/<int:task_id>/', views.task_view, name='task_view'),
    path('tasks/', views.task_list, name='task_list'),
    path('task/<int:task_id>/complete/', views.complete_task, name='complete_task'),


    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
