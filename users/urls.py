from users import views as users_views

from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

import recipes
from recipes.views import about, home
from . import views

app_name = "users"

urlpatterns = [
    # path('', recipes/home.html, name="home"),
    # path('about/',recipes/about.html, name="about"),
    # path('register/', users_views.register, name='register'),
    # path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('admin/', admin.site.urls),
    path('', include('recipes.urls')),
    path('register/', user_views.register, name="user-register"),
]