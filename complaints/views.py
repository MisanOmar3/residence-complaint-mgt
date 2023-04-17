from django.shortcuts import render
from rest_framework import generics, permissions, status

from students import serializers
from .models import Complaint
from .serializers import ComplaintSerializer, RegisterComplaintSerializer, ReviewComplaintSerializer
from rest_framework.response import Response


class ComplaintCreateView(generics.CreateAPIView):
    queryset = Complaint.objects.all()
    serializer_class = RegisterComplaintSerializer
    permission_classes = [permissions.IsAuthenticated]
    def post(self, reqquest):
        serializer = self.serializer_class(data=reqquest.data)
        if serializer.is_valid(raise_exception=True):
            details = serializer.save()
            
        
        
        return Response({
            "complaint": ComplaintSerializer(details, context=self.get_serializer_context()).data,
        }, status=status.HTTP_200_OK)

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

class ComplaintReviewView(generics.UpdateAPIView):
    queryset = Complaint.objects.all()
    serializer_class = ReviewComplaintSerializer
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
