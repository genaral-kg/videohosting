from rest_framework import serializers
from .models import Category, Material


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class MaterialListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Material
        fields = ('title', 'year', 'category')


class MaterialDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Material
        fields = '__all__'


class MaterialCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Material
        fields = ('title', 'year', 'video', 'desc', 'image', 'category')

