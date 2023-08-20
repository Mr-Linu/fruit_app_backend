from datetime import timedelta
from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework import status, permissions
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.tokens import PasswordResetTokenGenerator

from user.models import AppUser, Profile
from user.otp_email import send_otp_via_mail, send_registration_mail
from user.serializer import AppUserSerializer, MyTokenObtainPairSerializer, RegisterUserSerializer, UserProfileSerializer

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
                send_otp_via_mail(serializer.data['email'])
                print(1)
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
                # send_otp_via_mail(data['email'], data['full_name'])
                print(5)
                return Response(
                    serializer.data,
                    status = status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return e
        


class LoginView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer



class ProfileView(APIView):
    
    def get(self, request, id, format=None):
        try:
            user = AppUser.objects.get(id=id)
            profile = Profile.objects.get(user=user)
        except (AppUser.DoesNotExist, Profile.DoesNotExist):
            return Response({'Message': "User profile not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = RegisterUserSerializer(profile)
        return Response(serializer.data, status=status.HTTP_200_OK)
