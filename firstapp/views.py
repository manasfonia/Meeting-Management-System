from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render


# Create your views here.
def DisplayView(request):
    return render(request, "base.html")
