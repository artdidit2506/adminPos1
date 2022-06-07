from django.shortcuts import render
from django.apps import apps

# Create your views here.
def index(request):
    return render(request, 'base/index.html')

def users(request):
    return render(request, 'base/users-profile.html')

def pagesFaq(request):
    return render(request, 'base/pages-faq.html')

def pagesContact(request):
    return render(request, 'base/pages-contact.html')

def pagesRegister(request):
    return render(request, 'base/pages-register.html')

def pagesLogin(request):
    return render(request, 'base/pages-login.html')

def pagesError(request):
    return render(request, 'base/pages-error-404.html')

def pagesBlank(request):
    return render(request, 'base/pages-blank.html')

def componentsAlerts(request):
    return render(request, 'base/components/alerts.html')

def componentsAccordiants(request):
    return render(request, 'base/components/accordiants.html')

def componentsBadges(request):
    return render(request, 'base/components/badges.html')

def componentsBreadcrumbs(request):
    return render(request, 'base/components/breadcrumbs.html')

def componentsButtons(request):
    return render(request, 'base/components/buttons.html')
# Form
def formElements(request):
    return render(request, 'base/forms/elements.html')

def formLayouts(request):
    return render(request, 'base/forms/layouts.html')

def formEditors(request):
    return render(request, 'base/forms/editors.html')

def formValidation(request):
    return render(request, 'base/forms/validation.html')

# Tables
def formGeneral(request):
    return render(request, 'base/tables/tables-general.html')

def formData(request):
    return render(request, 'base/tables/tables-data.html')

# Charts

def formChartjs(request):
    return render(request, 'base/charts/charts-chartjs.html')

def formApexcharts(request):
    return render(request, 'base/charts/charts-apexcharts.html')

def formEcharts(request):
    return render(request, 'base/charts/charts-echarts.html')

# Icons

def formIconsbootstrap(request):
    return render(request, 'base/icons/icons-bootstrap.html')

def formIconsremix(request):
    return render(request, 'base/icons/icons-remix.html')

def formIconsboxicon(request):
    return render(request, 'base/icons/icons-boxicons.html')