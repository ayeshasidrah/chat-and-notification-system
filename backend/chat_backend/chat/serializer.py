from rest_framework import serializers
from django.contrib.auth import get_user_model

class UserGetserializer(serializers.ModelSerializer):
    class meta:
        model = get_user_model()
        fileds = ['email', 'frist_name', 'last_name', 'id']