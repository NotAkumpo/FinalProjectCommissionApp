from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.db.models import Sum
from django.views.generic.edit import FormMixin
from django.forms import inlineformset_factory

from .models import Commission, Job, JobApplication
from .forms import CommissionForm, JobForm, JobApplicationForm


class CommissionListView(ListView):
    model = Commission
    template_name = 'commissions_list.html'
    ordering = ['status','-created_at']
    

class CommissionDetailView(FormMixin, DetailView):
    model = Commission
    template_name = 'commissions_detail.html'
    form_class = JobApplicationForm
    
    def get_success_url(self):
        return reverse('commissions:commission-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        commission = self.get_object()
        total_manpower = commission.jobs.aggregate(total=Sum('manpowerRequired'))['total']
        context['has_jobs'] = commission.jobs.exists()
        context['total_manpower'] = total_manpower
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        commission = self.get_object()
        available_jobs = commission.jobs.all()
        kwargs['available_jobs'] = available_jobs
        kwargs['no_jobs'] = not self.object.jobs.exists()
        return kwargs

    def post(self, request, pk, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            jobApp = JobApplication()
            jobApp.job = form.cleaned_data.get('job')
            jobApp.applicant = self.request.user.profile
            jobApp.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class CommissionCreateView(LoginRequiredMixin, CreateView):
    model = Commission
    form_class = CommissionForm
    template_name = 'commissions_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['job_formset'] = JobInlineFormSet(self.request.POST)
        else:
            context['job_formset'] = JobInlineFormSet()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        job_formset = context['job_formset']
        if job_formset.is_valid():
            self.object = form.save()
            job_formset.instance = self.object
            job_formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form))

    def get_initial(self):
        return {'author': self.request.user.profile}

    def get_success_url(self):
        return reverse_lazy('commissions:commission-detail', kwargs={'pk': self.object.pk})


class CommissionUpdateView(LoginRequiredMixin, UpdateView):
    model = Commission
    form_class = CommissionForm
    template_name = 'commissions_update.html'

    def get_success_url(self):
        return reverse_lazy('commissions:commission-detail', kwargs={'pk': self.object.pk})


JobInlineFormSet = inlineformset_factory(
    Commission, Job, form=JobForm, extra=3, can_delete=True
)