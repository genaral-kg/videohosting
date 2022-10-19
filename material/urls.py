from django.urls import path, include, re_path
from rest_framework import permissions

from .views import MaterialViewSet
from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view
from drf_yasg import openapi




router = DefaultRouter()
router.register('material', MaterialViewSet)

urlpatterns = [
   path('', include(router.urls)),
]