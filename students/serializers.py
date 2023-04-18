from rest_framework import serializers
from .models import Student, User
from complaints.serializers import ComplaintSerializer
from complaints.models import Complaint
from rest_framework import status
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.utils.translation import gettext_lazy as _


#Serializer to get student data
class StudentsInformationSerializer(serializers.ModelSerializer):
  class Meta:
    model = Student
    fields = ('name', 'hall', 'room_number','matric','email',)
    
    
class StudentSerializer(serializers.ModelSerializer):
    # complaints = ComplaintSerializer(many = True)
    student = StudentsInformationSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = (
            "firstname",
            "lastname",
            "othername",
            "email",
            "student",
            # "complaints",  
    )

class StudentComplaintSerializer(serializers.ModelSerializer):
	complaints = ComplaintSerializer(many = True, read_only = True)
	class Meta:
		model = Student
		fields = (
			"complaints",
		) 

#Serializer to Get User Details for Login using Django Token Authentication
class StudentLoginSerializer(serializers.Serializer):
  email = serializers.EmailField(required=True, validators=[UniqueValidator])
  password = serializers.CharField(required=True)
  
  class Meta:
    fields = ("email", "password")
    extra_kwargs = {
        "password": {
            "write_only": True,
        }
    }

    def login(self, **kwargs):
        user = authenticate(**kwargs)

        if user and user.is_active:
            user = User.objects.get(email=user['email'])
            return {
              'id': user.id,
              'email': user.email,
              'status': status.HTTP_200_OK
            }
        return ValidationError(_("Incorrect credentials"))

class MyTokenObtainPairserializer(TokenObtainPairSerializer):
  @classmethod
  def get_token(cls, user):
      token = super().get_token(user)

      # Add custom claims
      token['email'] = user.email
      # ...

      return token

    
      
    
#Serializer to Register User
class StudentRegisterSerializer(serializers.ModelSerializer):
  """matric = serializers.CharField(
    required=True,
    validators=[UniqueValidator(queryset=Student.objects.all())]
  # )"""
  password = serializers.CharField(
    write_only=True, required=True, validators=[validate_password])
  password2 = serializers.CharField(write_only=True, required=True)
  student = StudentsInformationSerializer()
  class Meta:
    model = User
    fields = (
            "username",
            "firstname",
            "lastname",
            "othername",
            "email",
            "gender",
            "student",
            "password",
            "password2",
            # "profile_picture",
            
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
    student = validated_data.pop('student')
    user = User.objects.create(
        username = validated_data['username'],
        email=validated_data['email'],
        password=validated_data['password'],
        firstname=validated_data['firstname'],
        lastname=validated_data['lastname'],
        othername=validated_data['othername'],
        gender=validated_data['gender'],
        # profile_picture=validated_data['profile_picture'],
    )
    Student.objects.create(user=user, **student)
    return user
