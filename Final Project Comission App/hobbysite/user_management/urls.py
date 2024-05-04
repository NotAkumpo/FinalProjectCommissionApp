from django.urls import path

from .views import ProfileUpdateView, DashboardView, UserCreateView, ProfileCreateView


urlpatterns = [
    path('', ProfileUpdateView.as_view(), name='profile-update'),
    path('dashboard', DashboardView.as_view(), name='dashboard'),
    path('user/create', UserCreateView.as_view(), name='user-create'),
    path('profile/create', ProfileCreateView.as_view(), name='profile-create'),
    
]
app_name = 'user_management'
