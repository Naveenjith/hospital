from rest_framework.generics import ListCreateAPIView,CreateAPIView
from .models import Department,Doctor
from .serilaizers import Departmentserializer,Doctorserializer
# Create your views here.

class Departmentlistview(ListCreateAPIView):
    queryset=Department.objects.all()
    serializer_class=Departmentserializer

class Doctorlistview(CreateAPIView):
    queryset=Doctor.objects.all()
    serializer_class=Doctorserializer