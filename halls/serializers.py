from rest_framework import serializers
from .models import Hall
from students.models import Student
from students.serializers import StudentSerializer
from halladmin.serializers import HallAdminSerializer

class HallSerializer(serializers.ModelSerializer):
    halladmins = serializers.SlugRelatedField(read_only = True, slug_field = "name") #retrieves value from the Hall class
    students = serializers.PrimaryKeyRelatedField(many = True, read_only = True) #retrieves value from the Student class
    #complaints = 

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

       
   