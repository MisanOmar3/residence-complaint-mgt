from django.urls import path

from . import views

urlpatterns = [
    path('', views.ComplaintListView.as_view()),
    path('update/<int:pk>/', views.ComplaintUpdateView.as_view()),
    path('create/', views.ComplaintCreateView.as_view()),
    path('delete/<int:pk>/', views.ComplaintDeleteView.as_view())
]