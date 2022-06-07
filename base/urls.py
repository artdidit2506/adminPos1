from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('users/', views.users, name='users'),
    path('pages/', views.pages, name='pages'),
    path('alerts/', views.componentsAlerts, name='alerts'),
    path('accordiants/', views.componentsAccordiants, name='accordiants'),
]