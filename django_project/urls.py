"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.url')),
    path('register/',user_views.register, name='user-register'),
    path('login/',user_views.login, name='user-login'),
    path('logout/',user_views.logout, name='user-logout'),
    path('blood_request/',user_views.blood_request, name='user-blood_request'),
    path('profile/',user_views.profile, name='user-profile'),
    path('post/<int:post_id>/update',user_views.post_update, name='user-post_update'),
    path('post/<int:post_id>/delete',user_views.post_delete, name='user-post_delete')
]

