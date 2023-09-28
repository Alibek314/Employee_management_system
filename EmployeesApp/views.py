from django.contrib import messages
from django.contrib.auth import login
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect

from .forms import NewUserForm, NewDescendantForm
from .models import Employees

# Create your views here.


def all_employees(request):
    """
    Displays all employees in Tree form (recursetree used in template)
    """
    employees = Employees.objects.all()
    username = request.user.username
    return render(request, "EmployeesApp/all_employees.html", {
        "employees": employees,
        "username": username,
    })


def get_employee(request, emp_id):
    """
    Shows detailed employee information
    """
    employee = get_object_or_404(Employees, id=emp_id)
    username = request.user.username
    return render(request, "EmployeesApp/one_employee.html", {
        "employee": employee,
        "username": username,
    })


def show_team(request):
    """
    Shows list of all employees
    """
    team = Employees.objects.all()
    paginator = Paginator(team, 100)
    username = request.user.username
    if request.user.is_authenticated:
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
                "username": username,
            })
        else:
            page_obj = paginator.get_page(request.GET.get("page"))
            return render(request, "EmployeesApp/show_team.html", {
                "page_obj": page_obj,
                "username": username,
            })
    else:
        page_obj = paginator.get_page(request.GET.get("page"))
        return render(request, "EmployeesApp/team_stable.html", {
                    "page_obj": page_obj,
                    "username": username,
            })


def registration(request):
    """
    Default registration page(with custom user register form).
    """
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration complete")
            return redirect('hierarchy_route')

        messages.error(request, "Invalid data")
    form = NewUserForm()
    return render(request, "EmployeesApp/registration.html", {
        "register_form": form
    })


def redirect_company(request):
    """
    This view simply redirects client from rest_framework's default login page to 'hierarchy_route' url
    """
    return redirect('hierarchy_route')


def create_descendant(request, anc_id=None):
    """
    Adding new descendant employee to database
    """
    if request.method == "POST":
        if anc_id is not None:
            ancestor = Employees.objects.get(id=anc_id)
            form = NewDescendantForm(request.POST)
            form.save(ancestor=ancestor)
        else:
            form = NewDescendantForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect('team_route')
    else:
        form = NewDescendantForm()
        return render(request, "EmployeesApp/new_descendant.html", {
            "form": form,
        })




















