from django.db import models

# Create your models here.

class SeparatedValuesField(models.TextField):
    def __init__(self, *args, **kwargs):
        self.token = kwargs.pop('token', ',')
        super(SeparatedValuesField, self).__init__(*args, **kwargs)

    def to_python(self, value):
        if not value: return
        if isinstance(value, list):
            return value
        return value.split(self.token)

    def from_db_value(self, value, expression, connection, context):
        return self.to_python(self, value)
    def get_db_prep_value(self, value):
        if not value: return
        assert(isinstance(value, list) or isinstance(value, tuple))
        return self.token.join([unicode(s) for s in value])

    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        return self.get_db_prep_value(value)

class Job(models.Model):
    title = models.CharField(max_length=80)
    description = models.TextField(max_length=2000)
    addedOn = models.DateField(auto_now_add=True)
    def __unicode__(self):
        return self.title 
    def __str__(self):
        return self.title 

class Candidate(models.Model):
    name = models.CharField(max_length=80)
    email = models.CharField(max_length=80)
    contactNo = models.CharField(max_length=14)
    resumePath = models.FileField(upload_to='resumes/')
    appliedOn = models.DateField(auto_now_add=True)
    appliedFor = models.ForeignKey(Job, on_delete=models.CASCADE, verbose_name="job applied for")
    resumeMatched = models.DecimalField(null=True, decimal_places=2, max_digits=5)
    wcPath = models.FileField(null=True, upload_to='score_wc/') #word cloud
    
    def __unicode__(self):
        return self.name 
    def __str__(self):
        return self.name 
