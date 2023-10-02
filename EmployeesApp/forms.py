from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from EmployeesApp.models import Employees


# Create your forms here.

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class EmployeeForm(forms.ModelForm):
    parent_ID = forms.IntegerField(required=False)

    class Meta:
        model = Employees
        fields = ["name", "position", "salary", "photo"]


class DescendantForm(forms.ModelForm):
    class Meta:
        model = Employees
        fields = ["name", "position", "salary", "photo"]

    def save(self, commit=True, ancestor=None):
        employee = super(DescendantForm, self).save(commit=False)
        if ancestor is not None:
            employee.parent = ancestor
        if commit:
            employee.save()
        return employee
