from rest_framework import serializers
from .models import ESGProject, UserTask, CustomUser

class ESGProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = ESGProject
        fields = '__all__'  

class UserTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTask
        fields = '__all__' 


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email', 'role', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user