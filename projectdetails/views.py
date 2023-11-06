from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views.generic import CreateView

from django.urls import reverse_lazy
from .models import Project
from django.views.generic import UpdateView,ListView,DeleteView
from django.views.generic.base import TemplateView
from .forms import ProjectForm,CoordinatorForm,ProjectDeleteForm

class ProjectListView(LoginRequiredMixin,ListView):
    model = Project
    #queryset = Project.objects.filter(created_by=self.request.user)
    context_object_name = 'project'
    def get_queryset(self):
        queryset = super().get_queryset().filter(created_by=self.request.user)
        return queryset
class IndexView(TemplateView):
    template_name = 'index.html'

class ProjectCreateView(LoginRequiredMixin,CreateView):
    model = Project
    fields = ('project_title', 'email', 'tools', 'abstract')
    success_url = reverse_lazy('project_list')
    #template_name = 'projectdetails/project_update_form.html'
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class ProjectUpdateView(LoginRequiredMixin,UpdateView):
    slug_url_kwarg = 'uuid'
    slug_field = 'uuid' 
    model = Project
    form_class = ProjectForm
    #template_name = 'projectdetails/project_update_form.html'
    success_url = reverse_lazy('project_list')
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()

        if self.object.created_by == str(self.request.user):
            return super().get(request, *args, **kwargs)
        return redirect( success_url)
class ProjectDeleteView(LoginRequiredMixin,DeleteView):
    slug_url_kwarg = 'uuid'
    slug_field = 'uuid' 
    model = Project
    form_class = ProjectDeleteForm
    context_object_name = 'project'
    template_name = 'projectdetails/project_delete_form.html'
    success_url = reverse_lazy('project_list')
    def delete(self, request, *args, **kwargs):
        """
        Call the delete() method on the fetched object and then redirect to the
        success URL.
        """
        self.object = self.get_object()
        success_url = self.get_success_url()

        if self.object.created_by == str(self.request.user):
            
            self.object.delete()
            return redirect( success_url, ) # Also add id 

        return redirect( success_url)

class ProjectCoordinatorUpdateView(UpdateView):
    slug_url_kwarg = 'uuid'
    slug_field = 'uuid' 
    model = Project
    
    form_class = CoordinatorForm
    template_name = 'projectdetails/project_coordinator_update_form.html'
    success_url = reverse_lazy('project_list')
    

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
