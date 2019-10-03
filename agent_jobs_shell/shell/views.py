import requests

from django.shortcuts import render

from .forms import JobForm


def list_jobs(request):
    invalid_form = None
    
    if request.method == 'POST':
        form = JobForm(request.POST, request.FILES)
        
        if form.is_valid():
            print('VALID')
            print(form.cleaned_data)
        else:
            print('INVALID')
            invalid_form = form
    
    r = requests.get('https://localhost:8443/api/jobs', headers={'X-API-Key': 'b0efe4a6-3d6e-49a9-a249-f6362840aaf5'}, verify=False)
    jobs_data = r.json()
    
    return render(request, 'shell/list-jobs.html', 
        {'jobs': jobs_data, 'invalid_form': invalid_form})
