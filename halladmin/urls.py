from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


urlpatterns = [
    path('', views.HallAdminListView.as_view()),
    path('<int:pk>/update/', views.HalladminUpdateView.as_view()),
    path('login/', views.MyTokenObtainView.as_view(), name='access-token'),
    path('register/', views.RegisterHalladmintView.as_view()),
    
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]