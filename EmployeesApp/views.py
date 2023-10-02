from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect

from .forms import NewUserForm, DescendantForm, EmployeeForm
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
    Change employee information & save changes in DB
    """

    if request.method == "POST":
        employee = Employees.objects.get(id=emp_id)
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            employee = form.save(commit=False)
            if "parent_ID" in form.changed_data:
                employee.parent = Employees.objects.get(id=form.cleaned_data["parent_ID"])
            employee.save()
        return redirect('team_route')
    else:
        employee = get_object_or_404(Employees, id=emp_id)
        username = request.user.username
        form = EmployeeForm()
        return render(request, "EmployeesApp/one_employee.html", {
            "employee": employee,
            "username": username,
            "employee_form": form,
        })


def show_team(request):
    """
    Shows list of all employees. (sorted also)
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
    Registration page view.
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
    This view simply redirects client from rest_framework's default login page to 'hierarchy_route' url.
    """
    return redirect('hierarchy_route')


def create_descendant(request, anc_id=None):
    """
    Creating new descendant employee to database
    """
    if request.method == "POST":
        if anc_id is not None:
            ancestor = Employees.objects.get(id=anc_id)
            form = DescendantForm(request.POST)
            form.save(ancestor=ancestor)
        else:
            form = DescendantForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect('team_route')
    else:
        form = DescendantForm()
        return render(request, "EmployeesApp/new_descendant.html", {
            "form": form,
        })


def delete_employee(request, employee_id):
    """
    Deleting employee with resolving inheritance conflicts
    """
    employee = Employees.objects.get(id=employee_id)
    if employee.is_leaf_node():
        employee.delete()
    else:
        if len(employee.get_siblings()) >= 1:
            new_parent = employee.get_previous_sibling() or employee.get_next_sibling()
            for child in employee.get_children():
                child.move_to(target=new_parent)
                child.parent = new_parent
            employee.delete()
        else:
            new_parent = employee.parent
            for child in employee.get_children():
                child.move_to(target=new_parent)
                child.parent = new_parent
            employee.delete()
    return redirect('team_route')
