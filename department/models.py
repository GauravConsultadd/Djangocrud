from django.db import models
from employee.models import Employee

# Create your models here.
class Department(models.Model):
    name=models.CharField(max_length=100)
    manager=models.ForeignKey(Employee, null=False, on_delete=models.CASCADE)
    class Meta:
        db_table="department"