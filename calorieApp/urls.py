from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
     path('', views.index, name='home'),
    path('delete/<int:id>/', views.delete_food, name='delete'),
    path('reset/', views.reset, name='reset'),
]