from django.db import models

# Create your models here.


class Aadhar(models.Model):
    aadhar_no = models.CharField(max_length=12, unique=True)
    created_by = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return str(self.aadhar_no)
    
class Student(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    contact = models.CharField(max_length=10)
    aadhar = models.OneToOneField(Aadhar, on_delete=models.CASCADE)
    # aadhar = models.OneToOneField(Aadhar, on_delete=models.PROTECT)

    def __str__(self):
        return self.name
    

class Department(models.Model):
    d_name = models.CharField(max_length=20)
    d_head = models.CharField(max_length=20)

    def __str__(self):
        return self.d_name
    
class Employee(models.Model):
    e_name = models.CharField(max_length=20)
    e_email = models.EmailField()
    e_contact = models.CharField(max_length=10)
    # e_dep = models.ForeignKey(Department, on_delete=models.CASCADE)
    e_dep = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='dep')


    def __str__(self):
        return self.e_name
    

class Course(models.Model):
    title = models.CharField(max_length=50)
    def __str__(self):
        return self.title
    

class Member(models.Model):
    name = models.CharField(max_length=50)
    courses = models.ManyToManyField(Course)   # M2M relation
    def __str__(self):
        return self.name