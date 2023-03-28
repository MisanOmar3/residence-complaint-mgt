from .serializers import HallSerializer
from .models import Hall
from rest_framework import generics

class HallListView(generics.ListAPIView):
    serializer_class = HallSerializer
    queryset = Hall.objects.all()

class HallCreateView(generics.CreateAPIView):
    serializer_class = HallSerializer
    queryset = Hall.objects.all()