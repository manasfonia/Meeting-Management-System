from django.contrib import admin
from .models import EmployeeInfo, VisitorInfo

# Register your models here.

class EmployeeInfoAdmin(admin.ModelAdmin):
    list_display = ['user', 'designation', 'phone', 'office_address']

class VisitorInfoAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'address', 'host', 'timestamp', 'checkout']


admin.site.register(EmployeeInfo, EmployeeInfoAdmin)
admin.site.register(VisitorInfo, VisitorInfoAdmin)
