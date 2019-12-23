from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
            path('', LoginView.as_view(), name='login'),
            path('base/', views.DisplayView, name='base')

       ]
