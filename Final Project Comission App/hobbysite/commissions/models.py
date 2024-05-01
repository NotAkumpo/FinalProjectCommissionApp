from datetime import datetime
from django.db import models
from django.urls import reverse

# Create your models here.


class Commission(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    OPEN = "OPEN"
    FULL = "FULL"
    COMPLETED = "COMPLETED"
    DISCONTINUED = "DISCONTINUED"
    STATUS_CHOICES = {
        OPEN: "Open",
        FULL: "Full",
        COMPLETED: "Completed",
        DISCONTINUED: "Discontinued",
    }
    status = models.CharField(max_length=12,choices=STATUS_CHOICES,default=OPEN,)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
           return self.title

    def get_absolute_url(self):
           return reverse('commissions:commission-detail', args=[self.pk])

    def get_status(self):
        return self.status

    class Meta:
        ordering = ['created_at']
        verbose_name = 'Commission'
        verbose_name_plural = 'Comissions'


class Job(models.Model):
    commission = models.ForeignKey('Commission', on_delete=models.CASCADE, related_name='jobs')
    role = models.CharField(max_length=255, unique=True)
    manpowerRequired = models.IntegerField()

    OPEN = "OPEN"
    FULL = "FULL"
    STATUS_CHOICES = {
        OPEN: "Open",
        FULL: "Full",
    }
    status = models.CharField(max_length=4,choices=STATUS_CHOICES,default=OPEN,)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
           return self.role

    class Meta:
        ordering = ["-status", "-manpowerRequired", "role"]
        verbose_name = 'Job'
        verbose_name_plural = 'Jobs'


class JobApplication(models.Model):
    job = models.ForeignKey('Job', on_delete=models.CASCADE, related_name='jobApplications')
    applicant = models.ForeignKey('user_management.Profile', on_delete=models.CASCADE, related_name='jobApplications')

    PENDING = "PENDING"
    ACCEPTED = "ACCEPTED"
    REJECTED = "REJECTED"
    STATUS_CHOICES = {
        PENDING: "Pending",
        ACCEPTED: "Accepted",
        REJECTED: "Rejected",
    }
    status = models.CharField(max_length=8,choices=STATUS_CHOICES,default=PENDING,)

    applied_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-status", "-applied_at"]
        verbose_name = 'Job Application'
        verbose_name_plural = 'Job Applications'