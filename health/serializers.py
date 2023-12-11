from .models import CustomUser, Category, Data
from rest_framework import serializers

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'username', 'location', 'address', 'phone', 'role', 'password']
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user
    
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'user', 'name', 'description', 'additional_info', 'date_register']

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model= Data
        fields='__all__'