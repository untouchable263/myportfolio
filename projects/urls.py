from django.urls import path

from . import views

urlpatterns = [
    path('', views.ProjectView.as_view(), name='projects'),
    path('<int:pk>/', views.ProjectDetailView.as_view(), name='projectdetail'),
]