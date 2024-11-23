from django.urls import path
from .views import Departmentlistview,Doctorlistview

urlpatterns = [
    path('departments/',Departmentlistview.as_view(),name='deparment_list'),
    path('doctors/',Doctorlistview.as_view(),name='doctor_list')
]   