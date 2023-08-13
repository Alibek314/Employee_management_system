from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
# Create your models here.


class Employees(MPTTModel):
    name = models.CharField(max_length=50)
    position = models.TextField()
    hire_date = models.DateField()
    salary = models.PositiveIntegerField()
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return f'{self.name} - {self.position}'