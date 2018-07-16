from app1.models import User,Student,Teacher,Class,ClassStudent,Parents,Accountant,Section,SectionStudent,\
Syllabus,Subject

from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields=('full_name','addresss','phoneno','email','password','re_password','gender')

#
##Serializer Class for Student 
class StudentSerializer(serializers.HyperlinkedModelSerializer):
	user = UserSerializer()
	class Meta:
		model=Student
		fields=(
			'id',
			'father_name',
			'mother_name',
			'date_of_birth',
			'user',
			)

###Serializer Class for Teacher

class TeacherSerializer(serializers.HyperlinkedModelSerializer):
	user=UserSerializer()
	class Meta:
		model=Teacher
		fields=(
			
			'qualification',
			'user'

			)
####Serializer  To Add Class

class ClassSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model=Class
		fields=('id','name','max_capacity','description','image_1',)

#Serializer For Class Student

class ClassStudentSerializer(serializers.HyperlinkedModelSerializer):
	students = serializers.ListField()
	class Meta:
		fields=('students',)

#serializers For Parents

class ParentSerializer(serializers.HyperlinkedModelSerializer):
	user = UserSerializer()
	class Meta:
		model=Parents
		fields=(
			'user',

			)


class AccountantSerializer(serializers.HyperlinkedModelSerializer):
	user = UserSerializer()
	class Meta:
		model=Parents
		fields=(
			'user',

			)

class SectionSerializer(serializers.HyperlinkedModelSerializer):
	#user=UserSerializer()
	class_id=serializers.IntegerField()
	class Meta:
		model=Section
		fields=(
			'section_name','section_description','class_id'

			)

class SectionStudentSerializer(serializers.HyperlinkedModelSerializer):
	student_id = serializers.IntegerField()

	class Meta:
		model=SectionStudent
		fields=('student_id',)

class SyllabusSerializer(serializers.HyperlinkedModelSerializer):
	
	class Meta:
		model=Syllabus
		fields=(
			'title','description',

			)

class SubjectSerializer(serializers.HyperlinkedModelSerializer):
	syllabus_id=serializers.IntegerField()
	class Meta:
		model=Subject
		fields=(
			'subject_name','description','syllabus_id',

			)
	

