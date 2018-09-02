from django.contrib import admin

from .models import Student,Teacher,User,Class
####to Register models to admin
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(User)
admin.site.register(Class)

# Register your models here.
