from django.db import models
from django.contrib.auth import get_user_model
from datetime import date
import uuid
# from nltk.tokenize import word_tokenize

from students.models import Student
from halls.models import Hall

# Definition of the Complaints class
class Complaint(models.Model):
    categories = (
        ('carpentry','carpentry'),
        ('pest', 'pest'),
        ('plumbing', 'plumbing'),
        ('electrical','electrical'),
        ('other','other')
    )

    statuses = (
        ('Pending', 'Pending'),
        ('In progress', 'In progress'),
        ('Completed', 'Completed')
    )

    #defining the class variables
    complain_id = models.UUIDField(primary_key=True, null=False, blank=False, editable=False, default=uuid.uuid4)
    category = models.CharField(max_length = 15, blank=False, null=False, choices=categories)
    details = models.TextField(blank=True, null = True)
    #specifying a foreign key relationship with the Student class
    student = models.ForeignKey(Student, on_delete = models.CASCADE, related_name="complaints", null=False)
    submit_date = models.DateTimeField(auto_now_add=True)
    edited_date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length = 12, editable = True, blank=False, null=False, default="Pending", choices=statuses)
    #hall = models.ForeignKey(Hall, on_delete = models.CASCADE, to_field="name", related_name = "hall_complaints") #"""default = str(student.hall.name),"""
    #review = models.TextField(blank=True, null = True)

    #defining a property priority to Complaint instance
    @property
    def priority(self):
        stop_words = [
            "flood",
            "flooding",
            "flooded",
            "burn",
            "burnt",
            "burned",
            "fire",
            "melted",
            "melting",
            "lock",
            "locking",
            #---
            "socket",
            "sockets",
            "bed",
            "beds", 
            "light",
            "lights",
            "sink",
            "toilet",
            "door",
            
        ]

        if self.category == "pest":
            return "high"

        else:
            #checks the details of the complaint against the stop words listed, then assigns an appropriate priority value
            detail_words = self.details
            detail_words = detail_words.split(" ")
            for x in detail_words:
                for y in stop_words:
                    if x == y:
                        return "high"
            return "low"
        
        # for element, count in detail_words.items():
        #     if element  in stop_words and count>0:
        #         return "High"
        # return "Low"


    @property
    def hall(self):
        hall = str(self.student.hall.name)
        return hall

    @property
    def room_number(self):
        room_number = self.student.room_number
        return room_number
    @property
    def student_name(self):
        student_name = self.student.user.fullname
        return student_name
