from student.models import student
from django import forms


class stud(forms.ModelForm):
    class Meta:
        model = student 
        fields = ['__all__']
