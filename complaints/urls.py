from django.urls import path

from . import views

urlpatterns = [
    path('', views.ComplaintListView.as_view()),
    path('<int:pk>/update/', views.ComplaintUpdateView.as_view()),
    path('create/', views.ComplaintCreateView.as_view()),
    path('<int:pk>/delete/', views.ComplaintDeleteView.as_view())
]