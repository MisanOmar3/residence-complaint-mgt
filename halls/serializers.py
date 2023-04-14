from rest_framework import serializers
from .models import Hall
from students.models import Student
from students.serializers import StudentSerializer, StudentComplaintSerializer
from halladmin.serializers import HallAdminSerializer
from complaints.serializers import ComplaintSerializer

class HallSerializer(serializers.ModelSerializer):
    halladmins = serializers.SlugRelatedField(read_only = True, slug_field = "name") #retrieves value from the Hall class
    #students = serializers.SlugRelatedField(read_only = True, slug_field = "matric") #retrieves value from the Student class
    students = StudentSerializer(many = True)
    #students = serializers.SlugRelatedField(read_only=True, slug_field = "matric")#.fields[complaints]

    class Meta:
        #specifying the model and its fields to be serialized
        model = Hall
        fields = (
            "name",
            "halladmins",
            "students",
            #"complaints",
        )
    """@property
    def complaints(self):
        return students.complaints"""

class HallListSerializer(serializers.ModelSerializer):
    halladmins = serializers.SlugRelatedField(read_only = True, slug_field = "name") #retrieves value from the Hall class
    class Meta:
        model = Hall
        fields = (
            "name",
            "halladmins",
        )  

class HallComplaintSerializer(serializers.ModelSerializer):
    students = StudentComplaintSerializer(many = True)
    class Meta:
        model = Hall
        fields = (
            "name",
            "students",
        )   