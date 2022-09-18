from .models import Comment
from project.models import Project
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
# Create your views here.


def create(request,projectid):
    project = get_object_or_404(Project,pk = projectid)
    Ancomment = Comment()
    Ancomment.project = project
    Ancomment.user = request.user
    Ancomment.comment = 'this is a great project i will donate it'
    Ancomment.save()
    return HttpResponse('comment has been added')