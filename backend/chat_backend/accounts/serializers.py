from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate, password_validation
from django.contrib.auth.password_validation import validate_password
from rest_framework.exceptions import ValidationError

from .managers import UserManager as User
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer to register user. If a user is already registered, its displays user
    exist message
    """



    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data.get("first_name", ""),
            last_name=validated_data.get("last_name", "")
        )

        return user

    class Meta:
        model = get_user_model()
        fields = ['email', 'password', 'first_name', 'last_name']



class LoginSerializer(serializers.Serializer):
    """
        Serializer for user login
    """

    email = serializers.EmailField()
    password = serializers.CharField(max_length=255, write_only=True)

    def validate(self, data):
        user = authenticate(username=data['email'], password=data['password'])
        if not user:
            raise ValidationError('user not found')
        return user
