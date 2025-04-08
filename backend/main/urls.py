from django.urls import path
from . import views  # import your views here
from .api import hello_api

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('api/hello/', hello_api),
]
