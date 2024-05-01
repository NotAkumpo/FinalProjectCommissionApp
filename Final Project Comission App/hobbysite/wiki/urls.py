from django.urls import path
from .views import WikiListView, WikiDetailView

urlpatterns = [
    path('articles', WikiListView.as_view(), name = 'list'),
    path('article/<int:pk>', WikiDetailView.as_view(), name = 'wiki-detail')
]

app_name = 'wiki'