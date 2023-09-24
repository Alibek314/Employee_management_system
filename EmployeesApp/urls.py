from django.urls import path, re_path
from EmployeesApp import views


urlpatterns = [
    path('team/<int:emp_id>', views.get_employee, name='employee_detail'),
    re_path(r'^team$', views.show_team, name='team_route'),
    re_path(r'^$', views.all_employees, name='hierarchy_route'),
]
