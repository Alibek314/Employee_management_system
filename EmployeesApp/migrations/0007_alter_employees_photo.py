# Generated by Django 4.2.5 on 2023-10-02 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EmployeesApp', '0006_employees_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='photo',
            field=models.ImageField(blank=True, default='2037844.jpg', upload_to='photo/'),
        ),
    ]
