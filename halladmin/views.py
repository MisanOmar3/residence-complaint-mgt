from .serializers import HallAdminSerializer
from rest_framework import generics
from .models import HallAdmin

class HallAdminListView(generics.ListAPIView):
    serializer_class = HallAdminSerializer
    queryset = HallAdmin.objects.all()
