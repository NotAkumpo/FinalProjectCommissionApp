from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Commission, Job


class CommissionListView(ListView):
    model = Commission
    template_name = 'commissions_list.html'
    ordering = ['-status']
    

class CommissionDetailView(DetailView):
    model = Job
    template_name = 'commissions_detail.html'