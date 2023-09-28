from django.contrib.auth.models import User
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.urls import reverse
# Create your models here.


class Employees(MPTTModel):
    """
    Base model for all Employees
    """

    TRAINEE = "TR"
    JUNIOR = "JR"
    MIDDLE = "MD"
    SENIOR = "SR"
    LEAD = "LD"

    POSITION_CHOICES = [
        (TRAINEE, "Trainee"),
        (JUNIOR, "Junior"),
        (MIDDLE, "Middle"),
        (SENIOR, "Senior"),
        (LEAD, "Lead"),
    ]

    name = models.CharField(max_length=50)
    position = models.CharField(max_length=2, choices=POSITION_CHOICES, default=TRAINEE)
    hire_date = models.DateField(auto_now_add=True)
    salary = models.PositiveIntegerField()
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children',
    )

    def get_url(self):
        return reverse('employee_detail', args=[self.pk])

    def create_descendant(self):
        return reverse('new_descendant', args=[self.pk])

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return f'{self.name} - {self.position}'
