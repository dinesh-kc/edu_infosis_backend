"""pro1 URL Configuration

"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from app1 import views
from django.views.decorators.csrf import csrf_exempt ##for csrf error while creating

from rest_framework_nested import routers

##For Swagger
from rest_framework.permissions import AllowAny

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="EduInfosys API",
      default_version='v1',
      description="All apis",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="admin@belwasetech.com"),
      license=openapi.License(name="BSD License"),
   ),
   validators=['flex', 'ssv'],
   public=True,
   permission_classes=(AllowAny,),
)

router = routers.DefaultRouter()
router.register(r'students', views.StudentViewset)
router.register(r'teachers', views.TeacherViewset)###for Teacher
router.register(r'parents', views.ParentViewset)
router.register(r'class', views.ClassViewset, 'class')
router.register(r'section', views.SectionViewset, 'section')
router.register(r'accountant', views.AccountantViewset)
router.register(r'subject', views.SubjectViewset)
router.register(r'routine',views.RoutineViewset)
router.register(r'marksheet',views.SubjectMarkViewset)
router.register(r'barcode',views.BarcodeViewset)
router.register(r'payment',views.PaymentViewset)
router.register(r'exam',views.ExamViewset)
router.register(r'book',views.BookViewset)
router.register(r'images',views.MyPhotoViewset)
# router.register(r'syllabus',views.SyllabusViewset)
##router.register(r'class/(?P<id>[0-9]+)/student',  views.ClassStudentViewset, 'class-student')


class_router = routers.NestedSimpleRouter(router, r'class', lookup='class')
class_router.register(r'students', views.ClassStudentViewset, base_name='class-students')
class_router.register(r'section', views.ClassSectionViewset, base_name='class-sections')
class_router.register(r'syllabus', views.SyllabusViewset, base_name='class-syllabus')
class_router.register(r'subjects',views.SubjectViewset,base_name='class-subject')

#class_router.register(r'section', views.ClassSectionViewset, base_name='class-sections')


section_router = routers.NestedSimpleRouter(router, r'section', lookup='section')
section_router.register(r'student', views.SectionStudentViewset, base_name='section-students')
section_router.register(r'attendance',views.AttendanceViewset,base_name='section-attendance')

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^docs(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=None), name='schema-json'),
    url(r'^docs/$', schema_view.with_ui('swagger', cache_timeout=None), name='schema-swagger-ui'),
    url(r'^', include(router.urls)),
    url(r'^', include(class_router.urls)),
    url(r'^', include(section_router.urls)),
   
]

