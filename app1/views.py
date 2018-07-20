from django.shortcuts import render
#from django.contrib.auth.models import StdRegister
from app1.models import User, Student,Teacher,Class, ClassStudent,Parents,Accountant,Section,SectionStudent,\
Syllabus,Subject,Routine,SubjectMarks,SubMarkType,Barcode,Attendance,Payment
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.parsers import FormParser, MultiPartParser
import random
from app1.modules.barcode import Code128##For Barcode

from app1.serializers import StudentSerializer,TeacherSerializer, \
ClassSerializer,ClassStudentSerializer,ParentSerializer,AccountantSerializer,SectionSerializer,\
SectionStudentSerializer,SyllabusSerializer,SubjectSerializer,RoutineSerializer,SubjectMarksSerializer,\
BarcodeSerializer,AttendanceSerializer,PaymentSerializer

class StudentViewset(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        row = serializer.data
        user = row['user']

        if user['password'] != user['re_password']:
            return Response({'message':'pw not matched'})

        email = username = row['user']['email']
        
        user, created = User.objects.get_or_create(email=email, 
            defaults={'full_name':row['user']['full_name'],'addresss':row['user']['addresss'],
            'phoneno':row['user']['phoneno'],'password':row['user']['password'] ,'re_password':row['user']['re_password'],
            'gender':row['user']['gender'] ,'username':username})
        if created == False:
            return Response({'message':'Sorry the student is already registered.'})
       
        student = Student.objects.create(user_id=user.id)

        return Response(row)


    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.name = request.data.get("name")
        instance.save()

        serializer = self.get_serializer(instance)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)
            
            
    # def validate(self, data):
    #     if data.get('password') != data.get('re_password'):
    #         raise serializers.ValidationError("Those passwords don't match.")

    #     return data

    
class TeacherViewset(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

    def create(self,request):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        row=serializer.data
        email=username=row['user']['email']
        if user['password'] != user['re_password']:
            return Response({'message':'pw not matched'})


        user, created = User.objects.get_or_create(email=email, 
            defaults={'full_name':row['user']['full_name'],'addresss':row['user']['addresss'],
            'phoneno':row['user']['phoneno'],'password':row['user']['password'] ,'re_password':row['user']['re_password'],
            'gender':row['user']['gender'] ,'username':username})
        if created == False:
            return Response({'message':'sorry the Teacher is already exist'})
            
        teacher=Teacher.objects.create(user_id=user.id)
        return Response(row)

class ClassViewset(viewsets.ModelViewSet):
    queryset=Class.objects.all()
    serializer_class=ClassSerializer

    # @action(methods=['post'], detail=True)
    # def set_students(self, request, id=None):
    #     serializer=ClassStudentSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)

    #     row=serializer.data

    #     student_ids = row['students']
    #     for sid in student_ids:
    #         ClassStudent.objects.get_or_create(student_id=sid, Class_id=id)

    #     return Response(row)


class ClassStudentViewset(viewsets.ModelViewSet):
    queryset=ClassStudent.objects.all()
    serializer_class=ClassStudentSerializer

    def create(self, request, class_pk):

        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        row=serializer.data

        student_ids = row['students']
        for id in student_ids:
            ClassStudent.objects.get_or_create(student_id=id, _class_id=self.kwargs['class_pk'])
            
            return Response(id)




## For Parents


class ParentViewset(viewsets.ModelViewSet):
    queryset = Parents.objects.all()
    serializer_class = ParentSerializer

    def create(self,request):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        row=serializer.data
        #to verify password
        user=row['user']
        if user['password'] != user['re_password']:
            return Response({'message':'pw not matched'})


        email=username=row['user']['email']

        user, created = User.objects.get_or_create(email=email, 
            defaults={'full_name':row['user']['full_name'],'addresss':row['user']['addresss'],
            'phoneno':row['user']['phoneno'],'password':row['user']['password'] ,'re_password':row['user']['re_password'],
            'gender':row['user']['gender'] ,'username':username})
        if created == False:
            return Response({'message':'sorry the Parents is already exist'})
            
        parent=Parents.objects.create(user_id=user.id)
        return Response(row)

### For Accountant

class AccountantViewset(viewsets.ModelViewSet):
    queryset = Accountant.objects.all()
    serializer_class = AccountantSerializer

    def create(self,request):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        row=serializer.data
        #to verify password
        user=row['user']
        if user['password'] != user['re_password']:
            return Response({'message':'pw not matched'})


        email=username=row['user']['email']

        user, created = User.objects.get_or_create(email=email, 
            defaults={'full_name':row['user']['full_name'],'addresss':row['user']['addresss'],
            'phoneno':row['user']['phoneno'],'password':row['user']['password'] ,'re_password':row['user']['re_password'],
            'gender':row['user']['gender'] ,'username':username})

        if created == False:
            return Response({'message':'sorry the Parents is already exist'})
            
        parent=Parents.objects.create(user_id=user.id)
        return Response(row)

class ClassSectionViewset(viewsets.ModelViewSet):
    queryset=Section.objects.all()
    serializer_class=SectionSerializer

    def create(self,request, class_pk):
        serializer=self.get_serializer(data=request.data)
        #print(serializer)
        serializer.is_valid(raise_exception=True)
        row=serializer.data
        print(row)
        section_name=row['section_name']
       
        ## to check class id
        try:

            Class.objects.get(id=class_pk)

        except Exception as ex:
            return Response({'message':'sorry'+ str(ex)})
        else:
            Section.objects.get_or_create(_class_id=class_pk,section_name=section_name,
            defaults={'section_description':row['section_description']})
           
        return Response({'message':'created'})


class SectionViewset(viewsets.ModelViewSet):

    queryset=Section.objects.all()
    serializer_class=SectionSerializer

    def create(self,request):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        row=serializer.data
        Section.objects.get_or_create(_class_id=row['class_id'], section_name=row['section_name'],defaults={
            'section_description':row['section_description']})
        return Response(row)

class SectionStudentViewset(viewsets.ModelViewSet):
    queryset = SectionStudent.objects.all()
    serializer_class = SectionStudentSerializer

    def create(self,request,section_pk):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        row=serializer.data
        SectionStudent.objects.get_or_create(sec_id=section_pk,student_id=row['student_id'])

        return Response(row)

class SyllabusViewset(viewsets.ModelViewSet):
    queryset = Syllabus.objects.all()
    serializer_class = SyllabusSerializer

    def create(self,request,Class_pk):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        row=serializer.data
        Syllabus.objects.get_or_create(_class_id=Class_pk,defaults={'title':'title','description':'description'})

        return Response(row)


class SubjectViewset(viewsets.ModelViewSet):
    queryset=Subject.objects.all()
    serializer_class=SubjectSerializer

    def create(self,request):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        row=serializer.data
        Subject.objects.get_or_create(syllabus_id=syllabus_id,defaults={'subject_name':'subject_name','description':'description'})

class RoutineViewset(viewsets.ModelViewSet):
    queryset=Routine.objects.all()
    serializer_class=RoutineSerializer

    def create(self,request):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        row=serializer.data
        try:
            Section=Section.objects.get(section_pk)
            Teacher=Teacher.objects.get(teacher_pk)
            Subject=Subject.objects.get(subject_pk)
        except:
            return Response({'message':'sorry id doesnot exist'})
        else:
            Routine.objects.get_or_create(section_id=section_pk,subject_id=teacher_pk,teacher_id=subject_pk,
            defaults={'time_start':row['time_start'],'time_end':row['time_end']})
            return Response({'message':'created'})

class SubjectMarkViewset(viewsets.ModelViewSet):
    queryset=Routine.objects.all()
    serializer_class=SubjectMarksSerializer

    def create(self,request):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        row=serializer.data
        try:
            SubMarkType=SubMarkType.objects.get(SubMarkType_pk)

        except:
            return Response({'message':'sorry'})
        else:
            SubjectMarks.objects.get_or_create(_type_id=SubMarkType_pk,defaults={obtained_marks:row['obtained_marks'],marks_type:row['marks_type']})
        return Response({'Created Successfully'})


######Barcode#####
class BarcodeViewset(viewsets.ModelViewSet):
    queryset=Barcode.objects.all()
    serializer_class=BarcodeSerializer
    def create(self,request):
        upload_dir = 'app1/storage/barcodes/'
        try:
            os.makedirs(upload_dir)
        except:
            pass

        n = random.random()

        code = 'SMS-%s'%str(n)

        bar = Code128()
        bar.getImage(code,100,"png", path=upload_dir)

        b, c = Barcode.objects.get_or_create(bar_code=code, defaults={'file':upload_dir+code+'.png'})

        return b

class AttendanceViewset(viewsets.ModelViewSet):
    queryset=Attendance.objects.all()
    serializer_class=AttendanceSerializer
    parser_classes = (FormParser, MultiPartParser)

    def create(self,request,section_pk):
        #print(request.POST)
        #print(request.FILES)
        #serializer=self.get_serializer(data=request.POST)
        #serializer.is_valid(raise_exception=True)

        #files = request.FILES

        row=request.POST 
        # row=serializer.data
        try:
            _Section=Section.objects.get(sec_pk)
            _Student=Student.objects.get(student_pk)
        except:
            return Response("Sorry Sec id And Student id not found")
        else:
            Attendance.objects.get_or_create(sec_id=section_pk,student_id=student_pk,defaults={
                'status':row['status'],'date':row['date']
                })
            #'file':files['file'
            return Response("created")

    # def list(self, request, section_pk):
    #     data=request.get
    #     return Response([{'id':'testingingeisngie'}])

class PaymentViewset(viewsets.ModelViewSet):
    queryset=Payment.objects.all()
    serializer_class=PaymentSerializer

    def create(self,request):
        serializer=self.get_serializer(data=request.POST)
        serializer.is_valid(raise_exception=True)

        row=serializer.data
        
        Payment.objects.get_or_create(student_id=row['student_id'],defaults={
            'pay_amount':row['pay_amount'],'description':row['description'],'date_paid':row['date_paid']
            })
        return Response("created")
      