from django.urls import path

from . import views

urlpatterns = [
    path('', views.HallListView.as_view()),
    path('create/', views.HallCreateView.as_view()),
    path('<pk>/details/', views.HallDetailView.as_view()),
    path('complaints/', views.HallComplaintView.as_view()),
]