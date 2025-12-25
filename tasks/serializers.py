from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import Task
from django.contrib.auth.models import User

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'completed', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at', 'id']


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
        username=validated_data['username'],
        email=validated_data['email'],
        password=validated_data['password']
        )
        return user


class LoginSerializer(serializers.Serializer):
    # username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(
            # username=data["username"],
            username=data['email'],
            password=data["password"]
        )

        if not user:
            raise serializers.ValidationError("Invalid credentials")

        data["user"] = user
        return data