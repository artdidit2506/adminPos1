from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('users/', views.users, name='users'),
    path('pages/', views.pagesFaq, name='pages-faq'),
    path('pages-contact/', views.pagesContact, name='pages-contact'),
    path('alerts/', views.componentsAlerts, name='alerts'),
    path('accordiants/', views.componentsAccordiants, name='accordiants'),
    path('badges/', views.componentsBadges, name='badges'),
    path('breadcrumbs/', views.componentsBreadcrumbs, name='breadcrumbs'),
    path('buttons/', views.componentsButtons, name='buttons'),
    path('elements/', views.formElements, name='elements'),
    path('layouts/', views.formLayouts, name='layouts'),
    path('editors/', views.formEditors, name='editors'),
    path('validation/', views.formValidation, name='validation'),
    path('tables-general/', views.formGeneral, name='tables-general'),
    path('tables-data/', views.formData, name='tables-data'),
    path('chartjs/', views.formChartjs, name='charts-chartjs'),
    path('apexcharts/', views.formApexcharts, name='charts-apexcharts'),
    path('charts-echarts/', views.formEcharts, name='charts-echarts'),
    path('icons-bootstrap/', views.formIconsbootstrap, name='icons-bootstrap'),
    path('icons-remix/', views.formIconsremix, name='icons-remix'),
]