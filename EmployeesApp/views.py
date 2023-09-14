from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, HttpResponse
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

    if "Table-Order" in request.headers:
        sort_by = request.headers["Table-Order"].split(",")[1]
        page_num = int(request.headers["Table-Order"].split(",")[0])
        current_objects = paginator.get_page(page_num).object_list
        if sort_by == 'name':
            sorted_employees = sorted(current_objects, key=lambda x: x.name)
        elif sort_by == 'position':
            sorted_employees = sorted(current_objects, key=lambda x: x.position)
        elif sort_by == 'hire_date':
            sorted_employees = sorted(current_objects, key=lambda x: x.hire_date)
        elif sort_by == 'salary':
            sorted_employees = sorted(current_objects, key=lambda x: x.salary)
        else:
            sorted_employees = current_objects
        return render(request, "EmployeesApp/sorted_table.html", {
            "sorted_employees": sorted_employees,
        })

    else:
        page_obj = paginator.get_page(request.GET.get("page"))
        return render(request, "EmployeesApp/show_team.html", {
                    "page_obj": page_obj
            })
