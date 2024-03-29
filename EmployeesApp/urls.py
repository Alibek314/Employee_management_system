from django.urls import path, re_path
from EmployeesApp import views


urlpatterns = [
    path('team/new_member/<int:anc_id>', views.create_descendant, name='new_descendant'),
    path('team/delete_member/<int:employee_id>', views.delete_employee, name='delete_employee'),
    path('team/<int:emp_id>', views.get_employee, name='employee_detail'),
    re_path(r'^team$', views.show_team, name='team_route'),
    re_path(r'^$', views.all_employees, name='hierarchy_route'),
]
