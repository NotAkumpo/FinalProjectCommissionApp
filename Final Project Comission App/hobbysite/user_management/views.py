from django.shortcuts import render

# Create your views here.


from django.views.generic.edit import UpdateView
from .models import Profile
from .forms import ProfileForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'user_detail.html'
    success_url = '/admin'

    def get_object(self, queryset=None):
        return self.request.user.profile
