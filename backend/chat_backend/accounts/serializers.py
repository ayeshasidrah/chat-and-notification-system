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

    # email = serializers.EmailField(
    #     validators=[UniqueValidator(queryset=get_user_model().objects.all(),
    #                                 message="An account with the email already exists")])
    # password = serializers.CharField(required=True,
    #                                  validators=[password_validation.validate_password],
    #                                  style={'input_type': 'password'})

    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data.get("first_name", ""),
            last_name=validated_data.get("last_name", "")
        )
        print(user)

        return user

    class Meta:
        model = get_user_model()
        fields = ['email', 'password', 'first_name', 'last_name']
    # extra_kwargs = {'password': {'write_only': True}}


# class LoginSerializer(serializers.Serializer):
#     email = serializers.EmailField()
#     id = serializers.CharField(max_length=15, read_only=True)
#     password = serializers.CharField(max_length=255, write_only=True)
#
#     def validate(self, data):
#         email = data['email'].strip()
#         password = data['password'].strip()
#
#         if email is None:
#             raise serializers.ValidationError("Please provide an email to login")
#
#         if password is None:
#             raise serializers.ValidationError("Provide a password to login")
#
#       #  user = authenticate(username=email, password=password)
#         user = authenticate(username=data['email'], password=data['password'])
#
#
#         if user is None:
#             raise serializers.ValidationError("Invalid email or password")
#
#         if not user.is_active:
#             raise serializers.ValidationError("User is inactive")
#
#         # return {
#         #     "email": user.email,
#         #     "id": user.id
#         # }
#         return user

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
