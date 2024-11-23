from django.db import models

class Department(models.Model):
    name=models.CharField(max_length=100,unique=True)
    description=models.TextField(blank=True,null=True)

    def __str__(self):
        return self.name
    
class Doctor(models.Model):
    department=models.ForeignKey(Department,related_name='doctors',on_delete=models.CASCADE)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    specialization=models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"