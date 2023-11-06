from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from braces.views import SetHeadlineMixin,FormValidMessageMixin

from django.views.generic import CreateView
from .utils import get_batch
class L1CreateView(LoginRequiredMixin,SetHeadlineMixin,FormValidMessageMixin,CreateView):
    pass
    
    def form_valid(self, form):
        user=self.request.user
        batch=get_batch(user)
        form.instance.batch=batch
        form.instance.created_by = user
        return super().form_valid(form)  