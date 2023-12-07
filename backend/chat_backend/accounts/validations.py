from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
UserModel = get_user_model()

def validate_email(data):
    email = data['email'].strip()
    if not email:
        raise ValidationError('Please provide an email to login')
    return True

def validate_username(data):
    username = data['username'].strip()
    if not username:
        raise ValidationError('Choose a different username')
    return True

def validate_password(data):
    password = data['password'].strip()
    if not password:
        raise ValidationError('Provide a password to login')
    return True

def user_status():
    if not UserModel.is_active:
        raise ValidationError("User is inactive")