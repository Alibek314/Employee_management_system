from django.contrib import admin
from EmployeesApp.models import Employees

# Register your models here.


@admin.register(Employees)
class EmployeesAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'salary', 'hire_date']
