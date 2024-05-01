from django.contrib import admin

from .models import Commission, Job, JobApplication


class JobInLine(admin.TabularInline):
    model = Job


class CommissionAdmin(admin.ModelAdmin):
    model = Commission
    inlines = [JobInLine,]

    search_fields = ['title',]
    list_display = ['title', 'status',]
    list_filter = ['title', 'status',] 


class JobAdmin(admin.ModelAdmin):
    model = Job

    search_fields = ['role', 'commission',]
    list_display = ['role', 'commission', 'status', 'manpowerRequired']
    list_filter = ['role', 'commission',] 
    


class JobApplicationAdmin(admin.ModelAdmin):
    model = JobApplication

    search_fields = ['job', 'applicant',]
    list_display = ['job', 'applicant', 'status', 'applied_at']
    list_filter = ['job', 'applicant',] 


admin.site.register(Commission, CommissionAdmin)
admin.site.register(Job, JobAdmin)
admin.site.register(JobApplication, JobApplicationAdmin)