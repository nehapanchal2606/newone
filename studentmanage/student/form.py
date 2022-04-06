from django import forms
from .models import degree, department,student,semester,faculty, subject


class degForm(forms.ModelForm):
    class Meta:
        model = degree
        fields = '__all__'


class depForm(forms.ModelForm):
    class Meta:
        model = department
        fields = '__all__'


class stuForm(forms.ModelForm):
    class Meta:
        model = student
        fields = ['fn','ln','email','enrollment', 'deg_id', 'dep_id', 'sem_id', 'gender', 'parent_number','dob','qualification', 'image', 'password']


class facForm(forms.ModelForm):
    class Meta:
        model = faculty
        fields = '__all__'


class faForm(forms.ModelForm):
    class Meta:
        model = faculty
        fields = ['fn', 'ln', 'experience', 'email', 'qualification', 'dep_id', 'deg_id', 'sub_id', 'number']


class stForm(forms.ModelForm):
    class Meta:
        model = student
        fields = ['fn', 'ln', 'parent_number','enrollment','email','qualification', 'dep_id', 'deg_id', 'sem_id', 'number']


class semForm(forms.ModelForm):
    class Meta:
        model = semester
        fields = '__all__'


class subForm(forms.ModelForm):
    class Meta:
        model = subject
        fields = '__all__'