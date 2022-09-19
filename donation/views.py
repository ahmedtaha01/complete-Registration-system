from .models import Donation
from project.models import Project
from django.shortcuts import get_object_or_404 , redirect
from django.http import HttpResponse 
# Create your views here.



def create(request,projectid):
    if request.POST:
        project = get_object_or_404(Project,pk = projectid)
        donate = Donation()
        donate.project = project
        donate.user = request.user
        donate.amount = request.POST['amount']
        donate.save()
        return redirect('/project')