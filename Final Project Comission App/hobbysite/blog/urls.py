from django.urls import path

from .views import BlogListView, BlogDetailView


urlpatterns = [
    path('articles', BlogListView.as_view(), name='list'),
    path('article/<int:pk>', BlogDetailView.as_view(), name='blog-detail')
]
app_name = 'blog'
