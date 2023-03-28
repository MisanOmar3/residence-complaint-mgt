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
            "hall",
            "room_number",
            "submit_date",
            "edited_date",
        ]