from django.urls import path
from . import views  # import your views here

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
]
