from django.urls import path

from . import views

urlpatterns = [
    path('', views.StudentListView.as_view()),
    path('<int:pk>/update/', views.StudentUpdateView.as_view()),
    path('create/', views.StudentCreateView.as_view()),
    path('login/', views.StudentLoginView.as_view()),
    path('register/', views.RegisterStudentView.as_view()),
]