from rest_framework import serializers
from .models import Student
from complaints.serializers import ComplaintSerializer
from complaints.models import Complaint

from rest_framework import status
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

#Serializer to get student data
class StudentSerializer(serializers.ModelSerializer):
    complaints = ComplaintSerializer(many = True)
    class Meta:
        model = Student
        fields = (
            "firstname",
            "lastname",
            "othername",
            "matric",
            "email",
            # "hall",
            # "room_number",
            # "complaints",  
    )

#Serializer to Get User Details for Login using Django Token Authentication
class StudentLoginSerializer(serializers.ModelSerializer):
  class Meta:
    model = Student
    fields = ("email", "password")


#Serializer to Register User
class StudentRegisterSerializer(serializers.ModelSerializer):
  """matric = serializers.CharField(
    required=True,
    validators=[UniqueValidator(queryset=Student.objects.all())]
  )"""
  password = serializers.CharField(
    write_only=True, required=True, validators=[validate_password])
  password2 = serializers.CharField(write_only=True, required=True)
  class Meta:
    model = Student
    fields = (
            "firstname",
            "lastname",
            "othername",
            "matric",
            "email",
            "password2",
            "password",
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
    user = Student.objects.create(
      firstname=validated_data['firstname'],
      lastname=validated_data['lastname'],
      othername = validated_data['othername'],
      email=validated_data['email'],
      matric=validated_data['matric'],

    )
    user.set_password(validated_data['password'])
    user.save()
    return user