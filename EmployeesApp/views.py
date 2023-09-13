from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Employees
from django.views.generic import ListView
from django.http import JsonResponse

# Create your views here.


def is_ajax(request):
    return request.headers.get('X-Requested-With') == 'XMLHttpRequest'


def all_employees(request):
    emp = Employees.objects.all()
    return render(request, "EmployeesApp/all_employees.html", {
        "employees": emp
    })


def get_employee(request, emp_id):
    employee = get_object_or_404(Employees, id=emp_id)
    return render(request, "EmployeesApp/one_employee.html", {
        "employee": employee
    })


def show_team(request):
    team = Employees.objects.all()
    paginator = Paginator(team, 100)

    if is_ajax(request):
        sort_by = request.GET["sort_by"]
        page_num = request.GET["page_number"]
        first_index = (page_num * 100) - 100
        last_index = (page_num * 100) + 1
        sorted_employees = Employees.objects.order_by(sort_by)[first_index:last_index]
        return render(request, "EmployeesApp/show_team.html", {
            "page_obj": sorted_employees,
        })
    else:
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        return render(request, "EmployeesApp/show_team.html", {
                    "page_obj": page_obj
            })
