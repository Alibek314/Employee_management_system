from django.urls import path, re_path
from EmployeesApp import views
from EmployeesApp.views import ShowTeam

urlpatterns = [
    path('team/<int:emp_id>', views.get_employee, name='employee_detail'),
    re_path(r'^team$', ShowTeam.as_view()),
    re_path(r'^$', views.all_employees),
]
