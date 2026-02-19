from django.db import models

# Create your models here.
class Employee(models.Model):
    emp_name = models.CharField(max_length=100)
    emp_email = models.EmailField(unique=True)
    emp_position = models.CharField(max_length=50)
    emp_salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.emp_name