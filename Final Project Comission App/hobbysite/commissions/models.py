from datetime import datetime
from django.db import models
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class Commission(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    author = models.ForeignKey('user_management.Profile', on_delete=models.SET_NULL, null=True, related_name='commissions')
    openManpower = models.IntegerField(default=0)

    AOPEN = "AO"
    BFULL = "BF"
    CCOMPLETED = "CC"
    DDISCONTINUED = "DD"
    STATUS_CHOICES = {
        AOPEN: "Open",
        BFULL: "Full",
        CCOMPLETED: "Completed",
        DDISCONTINUED: "Discontinued",
    }
    status = models.CharField(max_length=13,choices=STATUS_CHOICES,default=AOPEN,)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('commissions:commission-detail', args=[self.pk])

    class Meta:
        ordering = ['created_at']
        verbose_name = 'Commission'
        verbose_name_plural = 'Commissions'


class Job(models.Model):
    commission = models.ForeignKey('Commission', on_delete=models.CASCADE, related_name='jobs')
    role = models.CharField(max_length=255)
    manpowerRequired = models.IntegerField()
    openManpower = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.openManpower = self.manpowerRequired
        super().save(*args, **kwargs)

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

    APENDING = "AP"
    BACCEPTED = "BP"
    CREJECTED = "CR"
    STATUS_CHOICES = {
        APENDING: "Pending",
        BACCEPTED: "Accepted",
        CREJECTED: "Rejected",
    }

    status = models.CharField(max_length=9,choices=STATUS_CHOICES,default=APENDING,)

    applied_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["status", "-applied_at"]
        verbose_name = 'Job Application'
        verbose_name_plural = 'Job Applications'


@receiver(post_save, sender=JobApplication)
def update_job_manpower(sender, instance, created, **kwargs):
    if instance.status == JobApplication.BACCEPTED:
        instance.job.openManpower -= 1
        if instance.job.openManpower == 0:
            instance.job.status = Job.FULL
        instance.job.save()


@receiver(post_save, sender=Job)
def update_commission_manpower(sender, instance, created, **kwargs):
    commission = instance.commission
    jobs = Job.objects.filter(commission=commission)
    commission.openManpower = sum(job.openManpower for job in jobs)
    if commission.openManpower == 0:
        commission.status = Commission.BFULL
    commission.save()