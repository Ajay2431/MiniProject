from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from braces.views import SetHeadlineMixin,FormValidMessageMixin
from django.http import HttpResponse
from django.views.generic import CreateView

from django.urls import reverse_lazy
from .models import Seminar
from django.views.generic import UpdateView,ListView,DeleteView
from django.views.generic.base import TemplateView
from .forms import SeminarForm,CoordinatorForm,SeminarDeleteForm
from .utils import get_batch
from .superviews import L1CreateView

class SeminarListView(LoginRequiredMixin, ListView):
    model = Seminar
    #queryset = Project.objects.filter(created_by=self.request.user)
    context_object_name = 'seminar'
    template_name = 'seminardetails/seminar_list.html'
    def get_queryset(self):
        queryset=super().get_queryset().filter(created_by=self.request.user)
        return queryset
    
class IndexView(TemplateView):
    template_name = 'index.html'

class SeminarCreateView(L1CreateView):
    #model = Seminar
    headline="Enter Your seminar"
    form_valid_message = "Seminar added Successfully"
    form_invalid_message = "Seminar adding failed"
    form_class = SeminarForm
    #fields = ('seminar_title', 'paper_link', 'upload_file')
    success_url = reverse_lazy('seminar_list')
    template_name = 'seminardetails/seminar_create_form.html'

class SeminarUpdateView(LoginRequiredMixin,UpdateView):
    slug_url_kwarg = 'uuid'
    slug_field = 'uuid' 
    model = Seminar
    form_class = SeminarForm
    template_name = 'seminardetails/seminar_update_form.html'
    success_url = reverse_lazy('seminar_list')
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        if str(self.object.created_by) == str(self.request.user):
            return super().get(request, *args, **kwargs)
        return redirect(success_url)
    
class SeminarDeleteView(LoginRequiredMixin,DeleteView):
    slug_url_kwarg = 'uuid'
    slug_field = 'uuid'
    model = Seminar
    #form_class = SeminarDeleteForm
    context_object_name = 'project'
    template_name = 'seminardetails/seminar_delete_form.html'
    success_url = reverse_lazy('seminar_list')
    
    def form_valid(self, form):
        user=str(self.request.user)
        uuid=self.kwargs["uuid"]
        created_by=str(Seminar.objects.filter(uuid=uuid)[0].created_by)

        if  created_by == user:
            return super().form_valid(form)
        return redirect(reverse_lazy("seminar_list"))
    
"""class SeminarCoordinatorListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    model = Seminar
    context_object_name = 'seminar'
    #queryset = Project.objects.filter(created_by=self.request.user)
    permission_required=('seminardetails.view_seminar')

    template_name = 'seminardetails/seminar_list.html'

class SeminarCoordinatorUpdateView(LoginRequiredMixin, UpdateView):
    slug_url_kwarg = 'uuid'
    slug_field = 'uuid' 
    model = Seminar
    from django.contrib.auth.models import Permission
    permissions = Permission.objects.filter(user=1)
    #print(permissions[0])
    perm_tuple = [x for x in Permission.objects.filter(user=1)]
    print(perm_tuple)

    form_class = CoordinatorForm
    template_name = 'seminardetails/seminar_coordinator_update_form.html'
    success_url = reverse_lazy('project_list')
    
    def form_valid(self, form):
        form.instance.approved_by = str(self.request.user)
        return super().form_valid(form)"""
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
