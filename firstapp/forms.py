from django import forms

from .models import EmployeeInfo, VisitorInfo

class VisitorForm(forms.ModelForm):

        model=Post
        fields=('Name', 'Address','PhoneNo','Email',)

        widgets={

        }
