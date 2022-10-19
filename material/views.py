from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from . import serializers

from material.models import Category, Material
from .serializers import CategorySerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_permissions(self):
        if self.action == 'POST':
            return [permissions.IsAdminUser()]
        return [permissions.AllowAny()]


class MaterialViewSet(ModelViewSet):
    queryset = Material.objects.all()
    filter_backends = (SearchFilter, DjangoFilterBackend)
    search_fields = ('title',)
    filterset_fields = ('category', )

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.MaterialListSerializer
        if self.action == 'POST':
            return serializers.MaterialCreateSerializer
        return serializers.MaterialDetailSerializer

    def get_permissions(self):
        if self.action in ('update', 'partial_update', 'destroy'):
            return [permissions.IsAdminUser()]
        return [permissions.IsAuthenticatedOrReadOnly()]








