from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import api_view, APIView
from rest_framework.response import Response
from .serializers import UserSerializer, LoginSerializer
from rest_framework import permissions, status
from django.contrib.auth import get_user_model, login, logout
from .validations import validate_email, validate_password, validate_username

# @api_view(['POST'])
# def register_user(request):
#     serializer = UserSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response({"message": "User signup successful."}, status=201)
#           #return Response(serializer.data, status=201)
#     return Response(serializer.errors, status=400)



class UserRegister(APIView):
    serializer_class = UserSerializer

    """
        Post view for user signup
    """
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User signup successful."}, status=201)
        return Response(serializer.errors, status=400)


# class UserLogin(APIView):
#     permission_classes = (permissions.AllowAny,)
#     authentication_classes = (SessionAuthentication,)
#
#     def post(self, request):
#         data = request.data
#         # assert validate_email(data)
#         # assert validate_password(data)
#         serializer = LoginSerializer(data=data)
#         if serializer.is_valid():
#             user = serializer.validate(data)
#             login(request, user)
#             return Response(serializer.data, status=status.HTTP_200_OK)


class UserLogin(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = (SessionAuthentication,)

    """
    Post view for user login using session authentication
    """
    def post(self, request):
        data = request.data
        assert validate_email(data)
        assert validate_password(data)
        serializer = LoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.validate(data)
            login(request, user)
            return Response({"message": "User logged in successfully."}, status=status.HTTP_200_OK)


class UserLogout(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

    def post(self, request):
        logout(request)
        return Response({"message": "User logged out successfully."}, status=status.HTTP_200_OK)