from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from halls.models import Hall
from students.models import User

#definition of the HallAdmin class
class HallAdmin(AbstractBaseUser):
    #declaring the class variables
    user = models.ForeignKey(User, blank=True, null=False, on_delete=models.CASCADE)
    hall = models.OneToOneField(Hall, on_delete = models.CASCADE, related_name="halladmins") #defining a one-to-one relationship with the Hall class
    staff_number = models.CharField(max_length=8, unique=True, null=False, default=None)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['email',]

    @property
    def name(self):
        name = self.user.lastname + " " + self.user.firstname
        if self.user.othername:
            name += " "+ self.user.othername
        return name

    def get_email(self):
        return self.user.email
>>>>>>> ec41c143c6d199f519295fa9694f78fcc881c137


    def __str__(self):
        return self.name
    #defining the objects attribute as an instance of the AdminManager class.

