"""
This module used to seed database with fake information.
"""
# import random
# import os
# import django
#
#
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Company.settings")
#
# django.setup()
#
# from EmployeesApp.models import Employees
#
# from faker import Faker
#
#
# faker = Faker()
#
# pos = [
#     'Trainee',
#     'Junior',
#     'Middle',
#     'Senior',
#     'Lead'
# ]
#
#
# def seeder(value):
#     for i in range(value):
#         name = faker.name()
#         position = random.choices(pos)[0]
#         hire_date = faker.date_this_decade()
#         salary = random.randint(500, 3000)
#         obj = Employees.objects.get_or_create(name=name, position=position, hire_date=hire_date, salary=salary)
#
#
# def main():
#     stop = int(input('Количество записей: '))
#     seeder(stop)
#
#
# if __name__ == '__main__':
#     main()
