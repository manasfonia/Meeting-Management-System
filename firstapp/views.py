from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.template import context

from .models import EmployeeInfo, VisitorInfo

# Create your views here.
def DisplayView(request):
    return render(request, "base.html")

def FixView(request):
    return render(request, "fixmeet.html")

def ProfileView(request):
    return render(request, "profile.html")

def EmView(request):
    model = EmployeeInfo
    context ={
        'designation': model.designation,
        'user': model.user,
        'phone': model.phone
    }
    return render(request, "employeedata.html")

def AddEmployer(request):
    return render(request, "addempolyer.html")
