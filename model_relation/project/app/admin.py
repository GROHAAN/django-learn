from django.contrib import admin
from .models import Student,Aadhar,Department,Employee,Course,Member
# Register your models here.

# admin.site.register(Student)
# admin.site.register(Aadhar)


admin.site.register(Department)
admin.site.register(Employee)

admin.site.register(Course)
admin.site.register(Member)