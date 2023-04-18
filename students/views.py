from rest_framework.response import Response
from rest_framework import generics, permissions,authentication
from rest_framework.views import APIView
from .models import Student, User
from complaints.models import Complaint
from complaints.serializers import ComplaintSerializer
from .serializers import (
    StudentsInformationSerializer, 
    StudentLoginSerializer, 
    StudentRegisterSerializer, 
    StudentSerializer,
    MyTokenObtainPairserializer,
    StudentComplaintSerializer,
    )
from rest_framework import status
# from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView
# from rest_framework.authtoken.models import Token


# Create your views here.


    
class MyTokenObtainView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairserializer

class StudentCreateView(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentsInformationSerializer
    def perform_create(self, serializer):
        if serializer.is_valid():
            instance_data = serializer.validated_data
            print(instance_data)
            serializer.save()
        
class StudentListView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentsInformationSerializer

class StudentComplaintListView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentComplaintSerializer
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (authentication.SessionAuthentication,)
    lookup_field = "pk"


class StudentUpdateView(generics.UpdateAPIView):
    queryset = Complaint.objects.all()
    serializer_class = ComplaintSerializer
    lookup_field = "pk"
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (authentication.SessionAuthentication,)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            
        return Response({
        "user": StudentSerializer(user, context=self.get_serializer_context()).data,
    }, status=status.HTTP_200_OK)

# Class based view to Get User Details using Token Authentication
class StudentLoginView(generics.GenericAPIView):
    serializer_class = StudentLoginSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.request.get('user')

        return Response({StudentSerializer(user, context=self.get_serializer_context()).data, status=status.HTTP_200_OK,
                        })

#Class based view to register user
class RegisterStudentView(generics.CreateAPIView):
  permission_classes = (permissions.AllowAny,)
  serializer_class = StudentRegisterSerializer

  def post(self, request):
    serializer = self.serializer_class(data=request.data)
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
       
    return Response({
        "user": StudentSerializer(user, context=self.get_serializer_context()).data,

    }, status=status.HTTP_201_CREATED)
