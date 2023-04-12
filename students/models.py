from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from halls.models import Hall
import uuid 

#Definition of a user manager for the student class

class User(AbstractBaseUser):    
    id = models.UUIDField(primary_key=True, editable=False, default = uuid.uuid4, db_index=True)
    email = models.EmailField(editable = True, unique = True, null = False)
    lastname = models.CharField(max_length=15, editable = True, blank = False, null = False)
    firstname = models.CharField(max_length=15, editable = True, blank = False, null = False)
    othername = models.CharField(max_length=15, editable = True, blank = True, null = True)

    @property
    def fullname(self):
        if self.othername:
            fullname = self.lastname + " " + self.firstname + " " + self.othername
        else:
            fullname = self.lastname + " " + self.firstname
        return fullname


class StudentUserManager(BaseUserManager):
    #Defining function for the creation of new users
    def create_user(self, lastname, firstname, othername, matric, email, hall, password):
        """
        Creates and saves a User with the given email and password.
        """
        #confirming that created user has matriculation number
        if not email:
            raise ValueError('Users must have email address.')

        #storing user attributes in a variable
        user = self.model(
            matric=self.matric,
            hall = self.hall,
            email = self.normalize_email(email),
            firstname = self.firstname,
            lastname = self.lastname,
            othername = self.othername
        )

        #the following methods are extended from BaseUserManager
        user.set_password(password)
        user.save(using=self._db)
        return user

#Definition of the student class
class Student(User):
    #defining class variables of Student
    """id = models.UUIDField(primary_key=True, editable=False, default = uuid.uuid4, db_index=True)
    firstname = models.CharField(max_length = 15, blank = False, null = False, editable = True)
    lastname = models.CharField(max_length = 15, blank = False, null = False, editable = True)
    othername = models.CharField(max_length = 15, blank = True, null = True, editable = True)
    email = models.EmailField(editable=True, unique=True, null=False)"""
    hall = models.ForeignKey(Hall, on_delete = models.CASCADE, related_name="students", blank=True, null=True, to_field="name") #defining a foreign key relation to the Hall class
    room_number = models.CharField(max_length = 4, editable = True, null=True, blank=True)
    matric = models.CharField(max_length = 7, unique = True) #setting primary key to matric number field

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['matric','email']
    

    """@property
    def name(self):
        name = self.lastname + " " + self.firstname 
        if self.othername:
            name+= " " + self.othername
        return name"""

    """@property
    def complaints(self):
        complaints = ComplaintSerializer(many = True)
        return complaints"""
    #defining the objects attribute as an instance of StudentUserManager class
    objects = StudentUserManager()
