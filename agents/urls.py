from django.urls import path
from . import views

urlpatterns = [
    path('', views.agent_list, name='agent_list'),
    path('<int:pk>/', views.agent_detail, name='agent_detail'),
]
