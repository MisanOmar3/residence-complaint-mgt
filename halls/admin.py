from django.contrib import admin

# Register your models here.
from .models import Hall
@admin.register(Hall)
class HallAdmin(admin.ModelAdmin):
    list_display = ('name',)