from django.shortcuts import render

# Create your views here.
from form_challenge.models import Project


def form_challenge(request):
    return render(request, 'index.html', {})

def form_challenge_index(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'project_index.html', context)

def form_challenge_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_details.html', context)