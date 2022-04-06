from django.db import models

# Create your models here.


class user(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=10)
    is_admin = models.IntegerField()


class degree(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200)


class department(models.Model):
    deg_id = models.ForeignKey(degree, on_delete=models.CASCADE)
    dep_name = models.CharField(max_length=30)
    dep_code = models.IntegerField()
    des = models.CharField(max_length=300)


class semester(models.Model):
    deg_id = models.ForeignKey(degree, on_delete=models.CASCADE)
    dep_id = models.ForeignKey(department, on_delete=models.CASCADE)
    sem_number = models.IntegerField()


class subject(models.Model):
    deg_id = models.ForeignKey(degree, on_delete=models.CASCADE)
    dep_id = models.ForeignKey(department, on_delete=models.CASCADE)
    sem_id = models.ForeignKey(semester, on_delete=models.CASCADE)
    sub_name = models.CharField(max_length=30)
    sub_code = models.IntegerField()
    sub_textbook = models.CharField(max_length=300)
    img = models.FileField()


class faculty(models.Model):
    GENDER = (
        ('1','MALE'),
        ('2','FEMALE')
    )
    HOD = (
        ('1','YES'),
        ('2','NO'),
    )
    email = models.EmailField()
    fn = models.CharField(max_length=30)
    ln= models.CharField(max_length=30)
    dep_id = models.ForeignKey(department, on_delete=models.CASCADE)
    deg_id = models.ForeignKey(degree, on_delete=models.CASCADE)
    sub_id = models.ForeignKey(subject, on_delete=models.CASCADE)
    gender = models.CharField(max_length=20, choices=GENDER)
    hod = models.CharField(max_length=10, choices=HOD)
    qualification = models.CharField(max_length=30)
    experience = models.IntegerField()
    number = models.CharField(max_length=10)
    image = models.FileField()


class student(models.Model):
    GENDER = (
        ('1', 'MALE'),
        ('2', 'FEMALE')
    )

    email = models.EmailField()
    fn = models.CharField(max_length=30)
    ln = models.CharField(max_length=30)
    enrollment = models.IntegerField()
    deg_id = models.ForeignKey(degree, on_delete=models.CASCADE)
    dep_id = models.ForeignKey(department, on_delete=models.CASCADE)
    sem_id = models.ForeignKey(semester, on_delete=models.CASCADE)
    gender = models.CharField(max_length=20, choices=GENDER)
    number = models.CharField(max_length=10)
    parent_number = models.CharField(max_length=10)
    dob = models.DateField()
    qualification = models.CharField(max_length=30)
    image = models.FileField()
    password = models.CharField(max_length=10)








