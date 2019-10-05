from django.db.models import Q

from rest_framework import status, generics, mixins, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from .permissions import ChatOwnerPermission, MessageOwnerPermission

from .models import Chat, TextMessage
from . import serializers


class ChatListAPIView(generics.ListAPIView):
    queryset = Chat.objects.all()
    serializer_class = serializers.ChatSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        qs = Chat.objects.get_all_user_chats(user)
        return qs


class ChatDetailAPIView(generics.RetrieveAPIView):
    lookup_field = 'id'
    queryset = Chat.objects.all()
    serializer_class = serializers.ChatSerializer
    permission_classes = (ChatOwnerPermission, permissions.IsAuthenticated,)


class MessageListAPIView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        chat_id = kwargs.get('id')
        chat_obj = None

        try:
            chat_obj = Chat.objects.get(id=chat_id)
        except:
            return Response(data={"detail": "Not found."}, status=404)


        return Response('jjj')
