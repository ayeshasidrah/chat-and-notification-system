from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes, APIView
from django.contrib.auth import get_user_model
from .serializer import UserGetserializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Message


User = get_user_model()


class ListUsers(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserGetserializer

    def get_user_list(self, request):
        try:
            user_obj = User.objects.exclude(id=request.user.id)
            serializer = self.serializer_class(user_obj, many=True)
            return Response(serializer.date)
        except Exception as e:
            print("Error getting list of users", str(e))
            return Response({"error": "Error getting list of users"}, status=400)


class MessageList(APIView):
    queryset = Message.objects.all()

    def chatPage(self, request, username):
        user_obj = User.objects.get(username=username)
        users = User.objects.exclude(username=request.user.username)

        if request.user.id > user_obj.id:
            thread_name = f'chat_{request.user.id}-{user_obj.id}'
        else:
            thread_name = f'chat_{user_obj.id}-{request.user.id}'
        message_objs = Message.objects.filter(thread_name=thread_name)
        return render(request, 'main_chat.html', context={'user': user_obj, 'users': users, 'messages': message_objs})

