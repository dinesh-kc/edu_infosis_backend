"""pro1 URL Configuration

"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from app1 import views
from django.views.decorators.csrf import csrf_exempt ##for csrf error while creating

from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register(r'student', views.StudentViewset)
router.register(r'teacher', views.TeacherViewset)###for Teacher
router.register(r'parents', views.ParentViewset)
router.register(r'class', views.ClassViewset, 'class')
router.register(r'section', views.SectionViewset, 'section')
router.register(r'accountant', views.AccountantViewset)
router.register(r'subject', views.SubjectViewset)
router.register(r'routine',views.RoutineViewset)
router.register(r'marksheet',views.SubjectMarkViewset)
router.register(r'barcode',views.BarcodeViewset)
router.register(r'payment',views.PaymentViewset)
# router.register(r'syllabus',views.SyllabusViewset)
##router.register(r'class/(?P<id>[0-9]+)/student',  views.ClassStudentViewset, 'class-student')


class_router = routers.NestedSimpleRouter(router, r'class', lookup='class')
class_router.register(r'student', views.ClassStudentViewset, base_name='class-students')
class_router.register(r'section', views.ClassSectionViewset, base_name='class-sections')
class_router.register(r'syllabus', views.ClassSectionViewset, base_name='class-sections')

#class_router.register(r'section', views.ClassSectionViewset, base_name='class-sections')


section_router = routers.NestedSimpleRouter(router, r'section', lookup='section')
section_router.register(r'student', views.SectionStudentViewset, base_name='section-students')
section_router.register(r'attendance',views.AttendanceViewset,base_name='section-attendance')

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^', include(class_router.urls)),
    url(r'^', include(section_router.urls)),
   
]

