from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add_employee, name='add_employee'),
    path('<int:employee_id>', views.view_employee, name='view_employee'),
    path('<int:employee_id>/delete', views.delete_employee, name='delete_employee'),
]
