from django.db import models
#from complaints.models import Complaint
# Definition of the Hall class
class Hall(models.Model):
    name = models.CharField(max_length = 30, null=False, primary_key=True)
