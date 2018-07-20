from app1.models import User,Student,Teacher,Class,ClassStudent,Parents,Accountant,Section,SectionStudent,\
Syllabus,Subject,Routine,SubMarkType,SubjectMarks,Barcode,Attendance,Payment

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

class RoutineSerializer(serializers.HyperlinkedModelSerializer):
	section_id=serializers.IntegerField()
	subject_id=serializers.IntegerField()
	teacher_id=serializers.IntegerField()

	class Meta:
		model=Routine
		fields=(
			'section_id','subject_id','teacher_id','time_start','time_end',

			)
class SubMarkTypeSerializer(serializers.HyperlinkedModelSerializer):
	subject_id=serializers.IntegerField()
	class Meta:
		model=SubMarkType
		fields=(
			'subject_id','marks_type','total_marks','pass_marks',
			)

class SubjectMarksSerializer(serializers.HyperlinkedModelSerializer):
	marks_type_detail=SubMarkTypeSerializer()
	_type_id=serializers.IntegerField()
	class Meta:
		model=SubjectMarks
		fields=(
			'_type_id','obtained_marks','marks_type_detail',
			)
	

class BarcodeSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model=Barcode
		fields=(
			'name',
			)
	

class AttendanceSerializer(serializers.HyperlinkedModelSerializer):
	sec_id=serializers.IntegerField()
	student_id=serializers.IntegerField()
	file = serializers.FileField()

	class Meta:
		model=Attendance
		fields=(
			'sec_id','student_id','status','date',#'file',

			)
	

class PaymentSerializer(serializers.HyperlinkedModelSerializer):
	student_id=serializers.IntegerField()
	class Meta:
		model=Payment
		fields=('student_id','pay_amount','description','date_paid',)



