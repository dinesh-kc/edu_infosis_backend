from django.shortcuts import render
#from django.contrib.auth.models import StdRegister
from app1.models import User, Student,Teacher,Class, ClassStudent,Parents,Accountant,Section,SectionStudent,Syllabus,Subject
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from app1.serializers import StudentSerializer,TeacherSerializer, \
ClassSerializer,ClassStudentSerializer,ParentSerializer,AccountantSerializer,SectionSerializer,\
SectionStudentSerializer,SyllabusSerializer,SubjectSerializer

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
            Class=Class.objects.get(class_pk)

        except:
            return Response({'message':'sorry'})
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

    