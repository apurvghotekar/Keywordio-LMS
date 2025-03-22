# library/serializers.py
from rest_framework import serializers
from .models import Book, Admin

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ['id', 'email', 'username', 'password']

    def create(self, validated_data):
        user = Admin.objects.create_user(**validated_data)
        return user
