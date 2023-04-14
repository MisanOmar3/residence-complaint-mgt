from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from students.models import User
from .models import HallAdmin

class HallAdminInformationSerializer(serializers.ModelSerializer):
    class Meta:
            model = HallAdmin
            fields = (
                "name",
                "staff_number",
                "hall",
                "get_email",
            )
class HallAdminSerializer(serializers.ModelSerializer):
    halladmin = HallAdminInformationSerializer(many=True, read_only=True)
    class Meta:
        model =User
        fields = (
            "firstname",
            "lastname",
            "othername",
            "email",
            "halladmin",
    )
        
        
class RegisterHallAdminSerializer(serializers.ModelSerializer):
    halladmin = HallAdminInformationSerializer()
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = User
        fields = (
                "username",
                "firstname",
                "lastname",
                "othername",
                "email",
                "gender",
                "halladmin",
                "password",
                "password2",
                "profile_picture",
                
        )
        extra_kwargs = {
        'firstname': {'required': True},
        'lastname': {'required':True},
        'email': {'required': True},
        }
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
            {"password": "Password fields didn't match."})
        return attrs
    def create(self, validated_data):
        halladmin = validated_data.pop('halladmin')
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            firstname=validated_data['firstname'],
            othername = validated_data['othername'],
            lastname=validated_data['lastname'],
            gender=validated_data['gender'],
            profile_picture=validated_data['profile_picture'],
        )
        HallAdmin.objects.create(user=user, **halladmin)
        return user
    
    
    
    


class MyTokenObtainPairserializer(TokenObtainPairSerializer):
  @classmethod
  def get_token(cls, user):
      token = super().get_token(user)

      # Add custom claims
      token['username'] = user.username
      # ...

      return token
  
  class Meta:
    model = HallAdmin
    fields = ("email", "password")