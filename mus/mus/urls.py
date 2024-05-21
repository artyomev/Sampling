
from django.contrib import admin
from django.urls import path, include

from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from analysis.views import ExecuteAnalysis
from projects.routers import router as project_router
from importfiles.views import FileUploadAPIView, SingleDownloadFile
from musauth.routers import router as user_router
from analysis.routers import router as analysis_router
# for homework 8
from projects.views import ProjectDetail, ProjectList

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('api/v1/', include(project_router.urls), name = r'projects' ),
    path('api/v1/', include(user_router.urls)),
    path('api/v1/', include(analysis_router.urls)),
    path('api/v1/upload/', FileUploadAPIView.as_view()),
    path('api/v1/download/<int:pk>/', SingleDownloadFile.as_view()),
    path('api/v1/execute/<int:pk>/',  ExecuteAnalysis.as_view()),
    # for homework 8
    path('api/v1/project_detail/<int:pk>/', ProjectDetail.as_view()),
    path('api/v1/project_list/', ProjectList.as_view()),
]
