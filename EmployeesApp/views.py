from django.shortcuts import render
from .models import Employees
# Create your views here.


def all_employees(request):
    emp = Employees.objects.all()

    return render(request, "EmployeesApp/all_employees.html", {
        "employees": emp
    })
