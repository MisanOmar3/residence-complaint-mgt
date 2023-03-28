from django.db import models
#from complaints.models import Complaint
# Definition of the Hall class
class Hall(models.Model):
    name = models.CharField(max_length = 30, null=False, primary_key=True)
    """@property
    def complaints(self):
        return Complaint.objects.all().filter(hall = self.name) #retrieves a list of all objects in the Complaint class whose hall attribute is equal to the name of the current hall object
"""