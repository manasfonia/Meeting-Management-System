from django.contrib import admin
from .models import EmployeeInfo

# Register your models here.

class EmployeeInfoAdmin(admin.ModelAdmin):
    list_display = ['user', 'designation', 'phone', 'office_address']


admin.site.register(EmployeeInfo, EmployeeInfoAdmin)
