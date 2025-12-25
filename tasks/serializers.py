from django.contrib.auth import authenticate, get_user_model
from rest_framework import serializers
from .models import Task, Profile

User = get_user_model()

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'completed', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at', 'id']


# class RegisterSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password']
#
#     def create(self, validated_data):
#         user = User.objects.create_user(
#         username=validated_data['username'],
#         email=validated_data['email'],
#         password=validated_data['password']
#         )
#         return user


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["id","bio", "avatar"]


class UserSerializer(serializers.ModelSerializer):    #read-only profile
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ["id", "email", "username", "profile"]



class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)



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