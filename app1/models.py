from django.db import models
from django.contrib.auth.models import AbstractUser

gender_choice = (
				('0','Select Gender'),
			    ('1','Male'),
			    ('2', 'Female'),
			    ('3','Other')
			    )

class BaseModel(models.Model):
	date_created = models.DateTimeField(auto_now_add=True)
	date_updated = models.DateTimeField(auto_now_add=True)

	class Meta:
		abstract = True

class User(AbstractUser, BaseModel):
	full_name = models.CharField(max_length=64)
	addresss=models.CharField(max_length=40)
	phoneno=models.IntegerField(null=True, blank=True)
	email=models.EmailField()
	password=models.CharField(max_length=40)
	re_password=models.CharField(max_length=40)


	gender=models.IntegerField(choices=gender_choice,default='0')

##models for student register
class Student(BaseModel):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	
	father_name=models.CharField(max_length=64)
	mother_name=models.CharField(max_length=60)
	date_of_birth=models.DateField(null=True)

	def __str__(self):
		return self.user.full_name

#model for teacher Register
class Teacher(BaseModel):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	
	qualification=models.CharField(max_length=60)

	def __str__(self):
		return self.user.full_name





###code to Register Class


class Class(BaseModel):
	name=models.CharField(max_length=50)
	max_capacity=models.IntegerField()
	description=models.TextField(max_length=120)
	image_1 = models.ImageField(blank=True,default='',upload_to='questions/')
		

class ClassStudent(BaseModel):
	student =models.ForeignKey(Student,on_delete=models.CASCADE)
	_class	= models.ForeignKey(Class,on_delete=models.CASCADE)		



class Parents(BaseModel):
	user=models.ForeignKey(User,on_delete=models.CASCADE)

class Accountant(BaseModel):
	user=models.ForeignKey(User,on_delete=models.CASCADE)

class Section(BaseModel):
	_class=models.ForeignKey(Class,on_delete=models.CASCADE)
	#user=models.ForeignKey(User,on_delete=models.CASCADE)
	section_name=models.CharField(max_length=40)
	section_description=models.TextField(max_length=120)

class SectionStudent(BaseModel):
	
	sec=models.ForeignKey(Section,on_delete=models.CASCADE)
	student=models.ForeignKey(Student,on_delete=models.CASCADE)


class Syllabus(BaseModel):
	title=models.CharField(max_length=65)
	description=models.TextField(max_length=13)
	_class=models.ForeignKey(Class,on_delete=models.CASCADE)


class Subject(BaseModel):
	subject_name=models.CharField(max_length=65)
	description=models.TextField(max_length=120)
	syllabus=models.ForeignKey(Syllabus,on_delete=models.CASCADE)
	

