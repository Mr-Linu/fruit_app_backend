from datetime import timedelta
from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework import status, permissions
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.tokens import PasswordResetTokenGenerator

from user.models import Profile
from user.serializer import AppUserSerializer, MyTokenObtainPairSerializer, RegisterUserSerializer

# class UserCreation(APIView):
#     def post(self, request):
#         data = request.data
#         return Response(se)



class CustomTokenGenerator(PasswordResetTokenGenerator):
    def token_valid_time(self):
        return timedelta(minutes=5).total_seconds()

default_token_generator = CustomTokenGenerator()

class RegisterView(GenericAPIView):
    serializer_class = AppUserSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        try:
            data=request.data
            serializer = AppUserSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                # send_registration_mail(serializer.data['email'])
                return Response(
                    serializer.data,
                    status = status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return e

# normal registration
class UserRegisterationView(APIView):
    serializer_class = RegisterUserSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        try:
            data=request.data
            print(1)
            serializer = RegisterUserSerializer(data=data)
            print(2)
            if serializer.is_valid():
                print(3)
                serializer.save()
                print(4)
                # send_registration_mail(serializer.data['email'])
                return Response(
                    serializer.data,
                    status = status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return e
        






class LoginView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer