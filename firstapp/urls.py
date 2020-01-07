from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
            path('', LoginView.as_view(), name='login'),
            path('logout/', views.logout, name='logout'),
            path('base/', views.DisplayView, name='base'),
            path('accounts/profile/getdata/<int:pk>', views.TimeOccupied, name='upcoming'),
            path('accounts/profile/fix/', views.FixView, name='fix'),
            path('accounts/profile/', views.ProfileView, name='profile'),
            path('accounts/profile/add', views.AddEmployer, name='add'),
            path('accounts/profile/add/<slug:username>/', views.RegisterEmployer, name='register'),
            path('accounts/profile/employdata', views.EmView, name='emdata'),
            path('accounts/profile/employdata/delete/<slug:username>/', views.DeleteEmployee, name='delete'),
            path('accounts/profile/employdata/update/<slug:username>/', views.UpdateEmployee, name='update'),
            path('accounts/profile/meetings/delete/<int:pk>/', views.DeleteVisitor, name='delete_visitor'),
            path('accounts/profile/meetings/update/<int:pk>/', views.UpdateVisitor, name='edit_visitor'),
            path('accounts/profile/meetings', views.ScheduleView, name='meetings'),
            path('accounts/profile/meet', views.UserMeeting, name='meet'),
            path('accounts/profile/info', views.UserUpdate, name='user_edit'),


       ]
