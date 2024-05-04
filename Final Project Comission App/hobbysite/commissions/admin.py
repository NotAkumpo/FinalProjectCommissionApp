from django.contrib import admin

from .models import Commission, Job, JobApplication


class JobInLine(admin.TabularInline):
    model = Job


class CommissionAdmin(admin.ModelAdmin):
    model = Commission
    exclude = ('author','openManpower')
    inlines = [JobInLine,]

    search_fields = ['title',]
    list_display = ['title', 'status',]
    list_filter = ['title', 'status',] 

    def save_model(self, request, obj, form, change):
        obj.author = request.user.profile
        super().save_model(request, obj, form, change)


class JobAdmin(admin.ModelAdmin):
    model = Job

    exclude = ['openManpower']
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