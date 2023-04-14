from django.db import models
from django.contrib.auth.models import UserManager, AbstractUser
from halls.models import Hall
from django.contrib.auth.validators import UnicodeUsernameValidator
import uuid
from django.utils.translation import gettext_lazy as _


#Definition of a user manager for the student class
username_validation = UnicodeUsernameValidator()

class User(AbstractUser):    
    
    GENDER_CHOICES = (('M', 'Male'),
                      ('F', 'Female'),)

    def profilePicture(instance, filename):
        user = AbstractUser.username
        return f'profile_pictures/{user}/picture {filename}'


    
    id = models.UUIDField(primary_key=True, editable=False, default = uuid.uuid4, db_index=True)
    firstname = models.CharField(_("first_name"), max_length=30, default='John')
    lastname = models.CharField(_("last_name"), max_length=30, default='Doe')
    email = models.EmailField(_("email"), unique=True,blank=False, default='default@gmail.com')
    othername = models.CharField(max_length=15, editable = True, blank = True, null = True)
    gender = models.CharField(choices=GENDER_CHOICES,max_length=6, default='M')
    profile_picture = models.FileField(upload_to=profilePicture, null=True, max_length=150, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    

    @property
    def fullname(self):
        if self.othername:
            fullname = self.lastname + " " + self.firstname + " " + self.othername
        else:
            fullname = self.lastname + " " + self.firstname
        return fullname


#Definition of the student class
class Student(models.Model):
    #defining class variables of Student
    user = models.ForeignKey(User, blank=True, null=False, on_delete=models.CASCADE, related_name="student")
    hall = models.ForeignKey(Hall, on_delete = models.CASCADE, related_name="students", blank=True, null=True, to_field="name") #defining a foreign key relation to the Hall class
    room_number = models.CharField(max_length = 4, editable = True, null=True, blank=True)
    matric = models.CharField(max_length = 7, unique = True) #setting primary key to matric number field

    @property
    def name(self):
        name = self.user.lastname + " " + self.user.firstname
        if self.user.othername:
            name += " "+ self.user.othername
        return name

    def email(self):
        return self.user.email
    
    
 