from rest_framework import serializers
from .models import Complaint
from students.models import Student

class ComplaintSerializer(serializers.ModelSerializer):

    class Meta:
        model = Complaint
        fields = [
            "category",
            "details",
            "status",
            "priority", 
            "student",
            "student_name",
            "hall",
            "room_number",
            "submit_date",
            "edited_date",
        ]
        
class RegisterComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complaint
        fields = ("category","student", "details")
        
        
        def create(self, validated_data):
            data = Complaint.objects.create(
                category= validated_data['category'],
                student= validated_data['student'],
                details= validated_data['details'],
            )
            data.save()
            return data
            