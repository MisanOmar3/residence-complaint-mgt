from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


urlpatterns = [
    path('', views.StudentListView.as_view()),
    path('<pk>/update/', views.StudentUpdateView.as_view()),
    path('create/', views.StudentCreateView.as_view()),
    path('login/', views.MyTokenObtainView.as_view(), name='access-token'),
    path('register/', views.RegisterStudentView.as_view()),
    path('<pk>/complaints/', views.StudentComplaintListView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]