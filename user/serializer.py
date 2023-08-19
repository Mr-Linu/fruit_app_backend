from django.db import transaction

from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from user.models import AppUser, Profile


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        token = self.get_token(self.user)
        data['user'] = str(self.user)
        data['id'] = self.user.id
        try:
            ownerobj = Profile.objects.get(user = self.user)
            data['full_name'] = ownerobj.full_name
            data['phone'] = ownerobj.phone
            data['Contact'] = ownerobj.Contact
            data['image'] = ownerobj.image
            data['is_verified'] = self.user.is_verified
        except Exception as e:
            pass
            
        
        return data


class AppUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=65,min_length=8,write_only=True)
    email = serializers.EmailField(max_length=255, )
    
    
    class Meta:
        model = AppUser
        fields = ('id','email', 'password', 'is_verified')

    def validate(self, attrs):
        email = attrs.get("email",'')
        if AppUser.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {'email':'Email is already in user'}
            )
        return super().validate(attrs)

    def create(self, validated_data):
        user = AppUser.objects.create_user(**validated_data)
        return user


class RegisterUserSerializer(AppUserSerializer):
    user = AppUserSerializer()
    
    class Meta:
        model = Profile
        fields = ('user','full_name', 'phone','contact','image' )

    def get_cleaned_data(self):
        return {
            'user.id':self.validated_data.get('user.id'),
            'full_name':self.validated_data.get('full_name'),
            'phone':self.validated_data.get('phone'),
            'contact':self.validated_data.get('contact'),
            'image':self.validated_data.get('image'),
        }

    @transaction.atomic
    def create(self, validated_data):

        user = validated_data.pop('user')
        
        email = user['email']
        password =user['password']
       
        user_instance = AppUser.objects.create_user(email=email,password=password)
        owner =Profile.objects.create(user =user_instance,**validated_data)
        
        owner.save()
        return owner