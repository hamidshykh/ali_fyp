from django.contrib import admin

from .models import Job
from .models import Candidate

# Register your models here.

class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

class CandidateAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'contactNo', 'resumePath', 'appliedOn', 'appliedFor', 'resumeMatched')

admin.site.register(Job, JobAdmin)
admin.site.register(Candidate, CandidateAdmin)



