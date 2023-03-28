from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from halls.models import Hall

#defining user manager for the HallAdmin class
class AdminManager(BaseUserManager):
    def create_user(self, lastname, firstname, othername, email, hall, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        #verifying that the user has an email before creation
        if not email:
            raise ValueError('Users must have email address')

        #storing data of the user into a reusable variable
        user = self.model(
            hall = self.hall,
            email = self.normalize_email(email),
            firstname = self.firstname,
            lastname = self.lastname,
            othername = self.othername
        )
        #the following methods are derived from the AbstractBaseUser class
        user.set_password(password)
        user.save(using=self._db)
        return user

#definition of the HallAdmin class
class HallAdmin(AbstractBaseUser):
    #declaring the class variables
    firstname = models.CharField(max_length = 15, blank = False, null = False, editable = True)
    lastname = models.CharField(max_length = 15, blank = False, null = False, editable = True)
    othername = models.CharField(max_length = 15, blank = True, null = True, editable = True)
    email = models.EmailField(editable=True, unique=True, null=False)
    hall = models.OneToOneField(Hall, on_delete = models.CASCADE, related_name="halladmins") #defining a one-to-one relationship with the Hall class

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['email']

    @property
    def name(self):
        name = self.lastname + " " + self.firstname
        if self.othername:
            name += " "+ self.othername
        return name

    def get_email(self):
        return self.email

    #defining the objects attribute as an instance of the AdminManager class.
    objects = AdminManager()

