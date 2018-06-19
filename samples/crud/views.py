from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Employee
from .forms import EmployeeForm
from django.urls import reverse
from django.contrib import messages

departments = ['sales', 'ops', 'hr', 'marketing', 'admin']
designations = ['clerk', 'manager', 'senior manager', 'director']


# Create your views here.

def delete_employee(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    employee.delete()

    messages.add_message(request, messages.INFO, '1 row deleted')
    return HttpResponseRedirect(reverse('index'))


def view_employee(request, employee_id):
    """view employee record"""
    try:
        employee = Employee.objects.get(pk=employee_id)
        context = dict(employee=employee)
    except Employee.DoesNot.Exist:
        raise Http404('Employee does not exist')

    return render(request, 'viewemp.html', context)


def index(request):
    """employee listing"""

    employees = Employee.objects.all()
    return render(request, 'index.html', dict(employees=employees))


def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']
            gender = form.cleaned_data['gender']
            department = form.cleaned_data['department']
            designation = form.cleaned_data['designation']

            e = Employee(name=name, age=age, gender=gender, department=department,
                         designation=designation)
            e.save()

            return render(request, 'viewemp.html', dict(employee=e))

    form = EmployeeForm()
    # return render(request, 'empform.html', dict(departments=departments, designations=designations))
    return render(request, 'empform2.html', dict(form=form))
