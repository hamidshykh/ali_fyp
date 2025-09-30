from django.forms import ModelForm

from .models import Candidate
from .models import Job

class CandidateForm(ModelForm):
    class Meta:
        model = Candidate
        fields = ['name', 'email', 'contactNo', 'resumePath', 'appliedFor']
        labels = {
            "contactNo": "Contact No ",
            "resumePath": "Resume/CV",
            "appliedFor": "Applying for "
        }
        
class JobForm(ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'description']
        labels = {
            "title": "Job Title",
            "description": "Job Description"
        }