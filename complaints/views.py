from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Complaint
from .serializers import ComplaintSerializer

class ComplaintCreateView(generics.CreateAPIView):
    queryset = Complaint.objects.all()
    serializer_class = ComplaintSerializer
    permission_classes = [permissions.IsAuthenticated]
    def perform_create(self, serializer):
        instance_data = serializer.validated_data
        serializer.save()

class ComplaintListView(generics.ListAPIView):
    queryset = Complaint.objects.all()
    serializer_class = ComplaintSerializer
    permission_classes = [permissions.IsAuthenticated]


class ComplaintUpdateView(generics.UpdateAPIView):
    queryset = Complaint.objects.all()
    serializer_class = ComplaintSerializer
    lookup_field = "pk"
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        instance_data = serializer.validated_data
        serializer.save()

class ComplaintDeleteView(generics.DestroyAPIView):
    queryset = Complaint.objects.all()
    serializer_class = ComplaintSerializer
    lookup_field = 'pk'
    permission_classes = [permissions.IsAdminUser]

    def perform_destroy(self, instance):
        #instance
        super().perform_destroy(instance)
