from django.contrib import admin
from .models import Student, User


# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('matric','hall', 'room_number')
    
@admin.register(User)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('username','fullname', 'email')