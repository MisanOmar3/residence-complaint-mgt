from django.db import models
#from complaints.models import Complaint
# Definition of the Hall class
class Hall(models.Model):
    
    hallName  =  (
        ('bethel splendor','bethel splendor'),
        ('queen esther', 'queen esther'),
        ('nelson mandela', 'nelson mandela'),
        ('felicia adebisi', 'felicia adebisi'),
        ('havila', 'havila'),
        ('samuel akande', 'samuel akande'),
        )
    
    
    name = models.CharField(choices=hallName,max_length = 30, null=False, primary_key=True)
    """@property
    def complaints(self):
        return Complaint.objects.all().filter(hall = self.name) #retrieves a list of all objects in the Complaint class whose hall attribute is equal to the name of the current hall object
"""