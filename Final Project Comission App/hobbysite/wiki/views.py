from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Article

# Create your views here.

class WikiListView(ListView):
    model = Article
    template_name = 'wiki_list.html'

class WikiDetailView(DetailView):
    model = Article
    template_name = 'wiki_detail.html'