from .serializers import (
    HallAdminSerializer, 
    RegisterHallAdminSerializer,
    MyTokenObtainPairserializer,
    )
from rest_framework import generics, permissions,authentication, status
from .models import HallAdmin
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response

class HallAdminListView(generics.ListAPIView):
    serializer_class = HallAdminSerializer
    queryset = HallAdmin.objects.all()

class MyTokenObtainView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairserializer
    
class RegisterHalladmintView(generics.CreateAPIView):
  permission_classes = (permissions.AllowAny,)
  serializer_class = RegisterHallAdminSerializer

  def post(self, request):
    serializer = self.serializer_class(data=request.data)
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
       
    return Response({
        "user": HallAdminSerializer(user, context=self.get_serializer_context()).data,

    }, status=status.HTTP_201_CREATED)

class HalladminUpdateView(generics.UpdateAPIView):

    lookup_field = "pk"
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (authentication.SessionAuthentication,)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            
        return Response({
        "user": HallAdminSerializer(user, context=self.get_serializer_context()).data,
    }, status=status.HTTP_200_OK)
