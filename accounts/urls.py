from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('user/dashboard/', views.user_dashboard, name='user_dashboard'),
    path('agent/dashboard/', views.agent_dashboard, name='agent_dashboard'),
    path('agent/profile/edit/<int:user_id>/', views.agent_profile_edit, name='agent_profile_edit'),
]
