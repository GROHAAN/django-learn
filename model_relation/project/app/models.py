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