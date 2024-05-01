from django.urls import path

from .views import MerchstoreListView, MerchstoreDetailView


urlpatterns = [
    path('items', MerchstoreListView.as_view(), name='list'),
    path('item/<int:pk>', MerchstoreDetailView.as_view(), name='merchstore-detail')
]
app_name = 'merchstore'
