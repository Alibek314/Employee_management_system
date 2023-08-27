from django.shortcuts import render, get_object_or_404
from .models import Employees
from django.views.generic import ListView


# Create your views here.


def all_employees(request):
    emp = Employees.objects.all()
    return render(request, "EmployeesApp/all_employees.html", {
        "employees": emp
    })


def get_employee(request, emp_id):
    employee = get_object_or_404(Employees, id=emp_id)
    return render(request, 'EmployeesApp/one_employee.html', {
        'employee': employee
    })


class ShowTeam(ListView):
    model = Employees
    paginate_by = 100
    template_name = 'EmployeesApp/show_team.html'
