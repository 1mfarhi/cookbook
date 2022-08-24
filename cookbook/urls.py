from django.urls import path
from cookbook import views


urlpatterns = [
    path("", views.home, name="home"),
]