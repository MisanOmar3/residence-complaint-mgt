from .serializers import HallSerializer, HallListSerializer
from .models import Hall
from rest_framework import generics

class HallListView(generics.ListAPIView):
    serializer_class = HallListSerializer
    queryset = Hall.objects.all()

class HallCreateView(generics.CreateAPIView):
    serializer_class = HallSerializer
    queryset = Hall.objects.all()

class HallDetailView(generics.RetrieveAPIView):
    serializer_class = HallSerializer
    queryset = Hall.objects.all()
    lookup_field = "pk"