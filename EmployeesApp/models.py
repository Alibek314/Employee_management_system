from django.db import models

# Create your models here.


class Employees(models.Model):
    name = models.CharField(max_length=50)
    position = models.TextField()
    hire_date = models.DateField()
    salary = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.name} - {self.position}'