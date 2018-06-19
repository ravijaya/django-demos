from django import forms

departments = ['sales', 'ops', 'hr', 'marketing', 'admin']
departments = [(dept, dept) for dept in departments]

designations = ['clerk', 'manager', 'senior manager', 'director']
designations = [(desg, desg) for desg in designations]


class EmployeeForm(forms.Form):
    name = forms.CharField(label='Name', required=True)
    age = forms.IntegerField(label='Age', required=True)
    gender = forms.CharField(label='Gender', required=True)
    department = forms.ChoiceField(label='Department', choices=departments)
    designation = forms.ChoiceField(label='Designation', choices=designations)

