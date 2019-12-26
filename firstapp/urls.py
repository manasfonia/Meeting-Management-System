from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
            path('', LoginView.as_view(), name='login'),
            path('base/', views.DisplayView, name='base'),
            path('accounts/profile/fix/', views.FixView, name='fix'),
            path('accounts/profile/', views.ProfileView, name='profile'),
            path('accounts/profile/employdata', views.EmView, name='emdata'),
            path('accounts/profile/add', views.AddEmployer, name='add_employer')
       ]
