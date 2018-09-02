# from app1.models import User,Student,Teacher,Class,ClassStudent,Parents,Accountant,Section,SectionStudent,\
# Syllabus,Subject,Routine,SubMarkType,SubjectMarks,Barcode,Attendance,Payment,Exam,Book,MyPhoto

# from rest_framework import serializers


# class UserSerializer(serializers.HyperlinkedModelSerializer):
# 	class Meta:
# 		model = User
# 		fields=('full_name','id','addresss','phoneno','email','gender',)

# class UserUpateSerializer(serializers.ModelSerializer):
# 	full_name=serializers.CharField(required=False)
# 	addresss=serializers.CharField(required=False)
# 	phoneno=serializers.IntegerField(required=False)
# 	class Meta:
# 		model=User
# 		fields=(
# 			'full_name',
# 			'addresss',
# 			'phoneno',
			
			
# 			)
# class UserPostSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model=User
# 		fields=('full_name','addresss')
# ##Serializer Class for Student 
# class StudentSerializer(serializers.HyperlinkedModelSerializer):
# 	user = UserPostSerializer()
# 	class Meta:
# 		model=Student
# 		fields=(
			
# 			# 'father_name',
# 			# 'mother_name',
# 			# 'date_of_birth',
# 			'user',
# 			)

# class StudentUpdateSerializer(serializers.ModelSerializer):
# 	user=UserUpateSerializer()
# 	father_name = serializers.CharField(required=False)
# 	mother_name = serializers.CharField(required=False)
# 	class Meta:
# 		model = Student
# 		fields = ('father_name','mother_name','user',)


# ###Serializer Class for Teacher

# class TeacherSerializer(serializers.HyperlinkedModelSerializer):
# 	user=UserSerializer()
# 	class Meta:
# 		model=Teacher
# 		fields=(
			
# 			'qualification',
# 			'user'

# 			)
# ####Serializer  To Add Class
# class TeacherUpdateSerializer(serializers.ModelSerializer):
# 	user=UserUpateSerializer()
# 	qualification=serializers.CharField(required=False)
# 	class Meta:
# 		model=Teacher
# 		fields=('qualification','user','id',)

# class ClassSerializer(serializers.HyperlinkedModelSerializer):
# 	class Meta:
# 		model=Class
# 		fields=('id','name','max_capacity','description',)

# #Serializer For Class Student
# class ClassUpdateSerializer(serializers.HyperlinkedModelSerializer):
# 	name=serializers.CharField(required=False)
# 	max_capacity=serializers.IntegerField(required=False)
# 	description=serializers.CharField(required=False)
# 	class Meta:
# 		model=Class
# 		fields=('id','name','max_capacity','description',)

# class ClassStudentSerializer(serializers.HyperlinkedModelSerializer):
# 	students = serializers.ListField()
	
# 	class Meta:
# 		model=ClassStudent
# 		fields=('students', )



# class ParentSerializer(serializers.HyperlinkedModelSerializer):
# 	user = UserSerializer()
# 	class Meta:
# 		model=Parents
# 		fields=(
# 			'id',
# 			'user',
			
# 			)
# class ParentUpdateSerializer(serializers.HyperlinkedModelSerializer):
# 	user=UserUpateSerializer()
# 	class Meta:
# 		model=Parents
# 		fields=('user','id',)


# class AccountantSerializer(serializers.HyperlinkedModelSerializer):
# 	user = UserSerializer()
# 	class Meta:
# 		model=Accountant
# 		fields=(
# 			'user','id',

# 			)
# class AccountantUpdatserializer(serializers.HyperlinkedModelSerializer):
# 	user=UserUpateSerializer()
# 	class Meta:
# 		model=Accountant
# 		fields=('user','id',)

# class SectionSerializer(serializers.HyperlinkedModelSerializer):
# 	#user=UserSerializer()
# 	# _class_id=serializers.SerializerMethodField()

# 	# def get_class_id(self, obj):
# 	# 	return obj._class_id
# 	#_class_id=serializers.IntegerField()
# 	class Meta:
# 		model=Section
# 		fields=(
# 			'id','section_name','section_description',

# 			)

# class SectionStudentSerializer(serializers.HyperlinkedModelSerializer):
# 	student_id = serializers.IntegerField()

# 	class Meta:
# 		model=SectionStudent
# 		fields=('student_id','id',)

# class SyllabusSerializer(serializers.HyperlinkedModelSerializer):
	
# 	class Meta:
# 		model=Syllabus
# 		fields=(
# 			'title','description','id',

# 			)

# class SubjectSerializer(serializers.HyperlinkedModelSerializer):
	
# 	class Meta:
# 		model=Subject
# 		fields=(
# 			'subject_name','description','id',

# 			)

# class RoutineSerializer(serializers.HyperlinkedModelSerializer):
# 	section_id=serializers.IntegerField()
# 	subject_id=serializers.IntegerField()
# 	teacher_id=serializers.IntegerField()

# 	class Meta:
# 		model=Routine
# 		fields=(
# 			'section_id','subject_id','teacher_id','time_start','time_end','id',

# 			)
# class SubMarkTypeSerializer(serializers.HyperlinkedModelSerializer):
# 	subject_id=serializers.IntegerField()
# 	class Meta:
# 		model=SubMarkType
# 		fields=(
# 			'subject_id','marks_type','total_marks','pass_marks','id',
# 			)

# class SubjectMarksSerializer(serializers.HyperlinkedModelSerializer):
# 	marks_type_detail=SubMarkTypeSerializer()
# 	_type_id=serializers.IntegerField()
# 	class Meta:
# 		model=SubjectMarks
# 		fields=(
# 			'_type_id','obtained_marks','marks_type_detail','id',
# 			)
	

# class BarcodeSerializer(serializers.HyperlinkedModelSerializer):
# 	class Meta:
# 		model=Barcode
# 		fields=(
# 			'name','id',
# 			)
	

# class AttendanceSerializer(serializers.HyperlinkedModelSerializer):
# 	#sec_id=serializers.IntegerField()
# 	student_id=serializers.IntegerField()
# 	date = serializers.CharField(source='date_created')
# 	#file = serializers.FileField()

# 	class Meta:
# 		model=Attendance
# 		fields=(
# 			'student_id','status','date',#'file', 
# 			'id',

# 			)
	

# class PaymentSerializer(serializers.HyperlinkedModelSerializer):
# 	student_id=serializers.IntegerField()
# 	class Meta:
# 		model=Payment
# 		fields=('student_id','pay_amount','description','id',)



# class ExamSerializer(serializers.HyperlinkedModelSerializer):
# 	class Meta:
# 		model=Exam
# 		fields=('name','id','date','description',)

# class BookSerializer(serializers.HyperlinkedModelSerializer):
	
# 	class Meta:
# 		model=Book
# 		fields=('name','isbn_no','publisher','edition','author','id',)

# class BookUpdateSerializer(serializers.HyperlinkedModelSerializer):
# 	name=serializers.CharField(required=False)
# 	author=serializers.CharField(required=False)
# 	description=serializers.CharField(required=False)

# 	class Meta:
# 		model=Book
# 		fields=('name','author','description','id',)


# class MyPhotoSerializer(serializers.HyperlinkedModelSerializer):
# 	class Meta:
# 		model=MyPhoto
# 		fields=('id','image',)