from django.shortcuts import render
from django.apps import apps

# Create your views here.
def index(request):
    return render(request, 'base/index.html')

def users(request):
    return render(request, 'base/users-profile.html')

def pages(request):
    return render(request, 'base/pages-faq.html')

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