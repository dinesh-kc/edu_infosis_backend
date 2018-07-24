from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.forms.fields import ImageField

gender_choice = (
				('0','Select Gender'),
			    ('1','Male'),
			    ('2', 'Female'),
			    ('3','Other')
			    )
marks_type_choice = (
				('0','Select MarksType'),
			    ('1','Theory'),
			    ('2', 'Practical')
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
	#image_1 = models.ImageField(blank=True,default='',upload_to='questions/')
		

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

class Routine(BaseModel):
	section=models.ForeignKey(Section,on_delete=models.CASCADE)
	subject=models.ForeignKey(Subject,on_delete=models.CASCADE)
	teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE)
	time_start=models.TimeField()
	time_end=models.TimeField()

class SubMarkType(BaseModel):
	subject=models.ForeignKey(Subject,on_delete=models.CASCADE)
	marks_type=models.IntegerField(choices=marks_type_choice,default=0)
	total_marks=models.IntegerField()
	pass_marks=models.IntegerField()

class SubjectMarks(BaseModel):
	_type=models.ForeignKey(SubMarkType,on_delete=models.CASCADE)
	obtained_marks=models.FloatField()

class Barcode(BaseModel):
	name=models.CharField(max_length=65)


def generateFilename(self,filename):
    url = 'storage/class/%s/%s'%(self.id,filename)
    return url

class Attendance(BaseModel):
	sec=models.ForeignKey(Section,on_delete=models.CASCADE)
	student=models.ForeignKey(Student,on_delete=models.CASCADE)
	status=models.BooleanField(default=False)
	date=models.DateField()
	#file = models.FileField(upload_to=generateFilename, blank=True, null=True)

class Payment(BaseModel):
	student=models.ForeignKey(Student,on_delete=models.CASCADE)
	pay_amount=models.IntegerField()
	description=models.TextField(max_length=200)
	date_paid=models.DateTimeField()
class Exam(BaseModel):
	name=models.CharField(max_length=65)
	date=models.DateTimeField()
	description=models.TextField(max_length=320)
	
class Book(BaseModel):
	name=models.CharField(max_length=65)
	author=models.CharField(max_length=65)
	description=models.CharField(max_length=300)
	_class=models.ForeignKey(Class,on_delete=models.CASCADE)



	
class MyPhoto(BaseModel):
	image = models.ImageField(upload_to='storage')

