from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Commission, Job
from .forms import CommissionForm


class CommissionListView(ListView):
    model = Commission
    template_name = 'commissions_list.html'
    ordering = ['status','created_at']
    

class CommissionDetailView(DetailView):
    model = Commission
    template_name = 'commissions_detail.html'


class CommissionCreateView(LoginRequiredMixin, CreateView):
    model = Commission
    form_class = CommissionForm
    template_name = 'commissions_create.html'
    success_url = '/commissions/list'


class CommissionUpdateView(LoginRequiredMixin, UpdateView):
    model = Commission
    form_class = CommissionForm
    template_name = 'commissions_update.html'
    success_url = '/commissions/list'