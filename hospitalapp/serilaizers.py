from rest_framework import serializers
from .models import Department,Doctor

class Departmentserializer(serializers.ModelSerializer):
    class Meta:
        model=Department
        fields=['id','name','description']

class Doctorserializer(serializers.ModelSerializer):
    class Meta:
        model=Doctor
        fields=['id','department', 'first_name', 'last_name', 'specialization']
