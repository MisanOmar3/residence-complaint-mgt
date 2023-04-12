from django.shortcuts import render

from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.views import APIView
from .models import Student, StudentUserManager
from complaints.models import Complaint
from complaints.serializers import ComplaintSerializer
from .serializers import StudentSerializer, StudentLoginSerializer, StudentRegisterSerializer
from rest_framework import status
from rest_framework.authentication import TokenAuthentication

class StudentCreateView(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    def perform_create(self, serializer):
        if serializer.is_valid():
            instance_data = serializer.validated_data
            print(instance_data)
            serializer.save()
        
class StudentListView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentUpdateView(generics.UpdateAPIView):
    queryset = Complaint.objects.all()
    serializer_class = ComplaintSerializer
    lookup_field = "pk"
    def perform_update(self, serializer):
        instance_data = serializer.validated_data
        serializer.save(instance_data)

# Class based view to Get User Details using Token Authentication
class StudentLoginView(APIView):
  authentication_classes = (TokenAuthentication,)
  permission_classes = (permissions.AllowAny,)
  def get(self,request,*args,**kwargs):
    user = Student.objects.get(email=request.user.id)
    serializer = StudentLoginSerializer(user)
    return Response(serializer.data)

#Class based view to register user
class RegisterStudentView(generics.CreateAPIView):
  permission_classes = (permissions.AllowAny,)
  serializer_class = StudentRegisterSerializer

  def post(self, request):
    serializer = self.serializer_class(data=request.data)
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
    return Response({'user': StudentSerializer(user, self.get_serializer_context()).data}, status=status.HTTP_201_CREATED,)