from django.db import models
from django.contrib.auth import get_user_model
from datetime import date
# from nltk.tokenize import word_tokenize

from students.models import Student
from halls.models import Hall

# Definition of the Complaints class
class Complaint(models.Model):
    categories = (
        ('carpentry','carpentry'),
        ('pest', 'pest'),
        ('plumbing', 'plumbing'),
        ('furniture','furniture',),
        ('electrical','electrical'),
        ('other','other')
    )

    statuses = (
        ('Pending', 'Pending'),
        ('In progress', 'In progress'),
        ('Completed', 'Completed')
    )

    #defining the class variables
    category = models.CharField(max_length = 15, blank=False, null=False, choices=categories)
    details = models.TextField(blank=True, null = True)
    #specifying a foreign key relationship with the Student class
    student = models.ForeignKey(Student, on_delete = models.CASCADE, related_name="complaints")
    submit_date = models.DateTimeField(auto_now_add=True)
    edited_date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length = 12, editable = True, blank=False, null=False, default="Pending", choices=statuses)
    #hall = models.ForeignKey(Hall, on_delete = models.CASCADE, to_field="name", related_name = "hall_complaints") #"""default = str(student.hall.name),"""

    #defining a property priority to Complaint instance
    @property
    def priority(self):
        stop_words = (
            "leaking",
            "leak",
            "leaks",
            "flood",
            "flooding",
            "flooded",
            "bedbug",
            "bedbugs",
            "rat",
            "rats",
            "bed",
            "burn",
            "burnt",
            "burned",
            "blew",
            "blow",
            "fire",
            "melted",
            "melting",
            "scattered",
            "scattering",
            "eaten",
            "lock",
            "locking",
        )
        #checks the details of the complaint against the stop words listed, then assigns an appropriate priority value
        detail_words = self.details
        for x in stop_words:
            if x in detail_words:
                return "high"
                break
            else:
                return "low"


    @property
    def hall(self):
        hall = str(self.student.hall.name)
        return hall

    @property
    def room_number(self):
        room_number = self.student.room_number
        return room_number
