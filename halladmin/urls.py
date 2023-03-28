from django.urls import path
from .serializers import HallAdminSerializer
from . import views

urlpatterns = [
    path('', views.HallAdminListView.as_view()),
]