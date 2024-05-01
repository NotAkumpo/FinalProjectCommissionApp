from django.urls import path

from .views import UserUpdateView


urlpatterns = [
    path('', UserUpdateView.as_view(), name='user-detail'),
]
app_name = 'user_management'
