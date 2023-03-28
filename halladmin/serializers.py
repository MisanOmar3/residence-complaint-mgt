from rest_framework import serializers
from .models import HallAdmin

class HallAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = HallAdmin
        fields = (
            "name",
            "email",
            "hall",
        )