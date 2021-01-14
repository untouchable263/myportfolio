from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from .models import Project

class ProjectView(generic.ListView):
    template_name = 'projects.html'
    context_object_name = 'item_list'

    def get_queryset(self):
        """
        Returns the list of all my projects
        """
        return Project.objects.all

class ProjectDetailView(generic.DetailView):
    model = Project
    template_name = 'detail.html'
    context_object_name = 'item'
