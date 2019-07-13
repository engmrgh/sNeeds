import datetime

from django.contrib.auth import authenticate, get_user_model

from rest_framework import status, permissions, generics, mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_jwt import utils as jwt_utils

from .utils import jwt_response_payload_handler
from .serializers import UserRegisterSerializer, UserSerializer
from .permissions import NotLoggedInPermission

User = get_user_model()


class AuthView(APIView):
    '''
    Post format:
        {
        "email":"bartararya@gmail.com",
        "password":"****:)"
        }
    '''

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return Response({'detail': 'You are already authenticated'}, status=400)

        data = request.data
        email = data.get('email')
        password = data.get('password')
        user = authenticate(email=email, password=password)

        if user:
            payload = jwt_utils.jwt_payload_handler(user)
            token = jwt_utils.jwt_encode_handler(payload)
            response = jwt_response_payload_handler(token, user=user, request=request)

            return Response(response, status=200)

        else:
            return Response({'detail': 'Invalid email/password'}, status=401)


class RegisterView(mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [NotLoggedInPermission]

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return Response({'detail': 'You are already authenticated'}, status=400)
        return self.create(request, *args, **kwargs)


class UserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_user(self, request):
        return request.user

    def get(self, request, *args, **kwargs):
        user = self.get_user(request)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        user = self.get_user(request)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
