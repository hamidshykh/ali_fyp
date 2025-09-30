from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from .forms import CandidateForm
from .forms import JobForm
from .application_profiler import JobApplicationsProfiler
from .models import Job
from .models import Candidate
from django.conf import settings
from django.shortcuts import redirect
import base64
from django.http import HttpResponse
from django.contrib.auth import logout
from django.template import RequestContext

# Create your views here.
from os.path import abspath

def job_applicaion(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CandidateForm(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():
            form = form.save()
            JobApplicationsProfiler(form).start()
            return JsonResponse({'data':'Data uploaded'})
        else:
            return JsonResponse({'data':'Something went wrong!!'})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CandidateForm()

    return render(request, 'jobapply2.html', {'form': form})

def view_job(request):
    data = Job.objects.all()
    data = {
        "jobs": data,
        "colors": ["blue", "green", "yellow", "brown", "purple" , "orange"]
    }
    return render(request, 'job.html', data)
    
def add_job(request):
    # if this is a POST request we need to process the form data
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = JobForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            return JsonResponse({'data':'Data uploaded'})
        else:
            return JsonResponse({'data':'Something went wrong!!'})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = JobForm()

    return render(request, 'addjob2.html', {'form': form})

def image_in_base64(data):
    print(data)
    with open(data['wcPath'], "rb") as image_file:
        ext = data['wcPath'].split('.')[-1]
        prefix = f'data:image/{ext};base64,'
        encoded_string = prefix + base64.b64encode(image_file.read()).decode('utf-8')
    data['wcPath'] = encoded_string
    return data

def view_result(request):
    #Candidate.objects.all().delete()
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    data = Job.objects.all()
    result = None
    if request.method == 'POST':
        of = request.POST.get("resultof")
        result = Candidate.objects.all().filter(appliedFor=of).values()
        #result = list(map(image_in_base64, result))
        return JsonResponse({'result':list(result)})
    data = {
        "jobs": data,
        "result": result
    }
    return render(request, 'result.html', data)

def pdf_view(request, p):
    print("sdsds", p)
    with open(p, 'rb') as pdf:
        response = HttpResponse(pdf.read(),content_type='application/pdf')
        response['Content-Disposition'] = ' inline; filename={}'.format(os.path.basename(path))
        return response
        
def log_out(request):
    logout(request)
    return redirect('%s?next=%s' % (settings.LOGIN_URL, "../../addjob/"))
    
# HTTP Error 404
def bad_request(request, exception):
    print("pppp")
    return render(request, 'nf.html', RequestContext(request)) 
