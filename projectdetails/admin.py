from django.contrib import admin

# Register your models here.
from .models import Project
admin.site.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project','created_by')
    actions = None

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'created_by', None) is None:
            obj.created_by = request.user
        obj.save()
