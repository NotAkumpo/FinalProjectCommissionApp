from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import ProductType, Product


class MerchstoreListView(ListView):
    model = Product
    template_name = 'merchstore_list.html'

class MerchstoreDetailView(DetailView):
    model = Product
    template_name = 'merchstore_detail.html'