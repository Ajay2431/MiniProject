from django.contrib import admin

# Register your models here.
from .models import Seminar,Batch,BatchUserMapping
admin.site.register(Seminar)
class BatchAdmin(admin.ModelAdmin):
  list_display = ("name", "active", "deactivation_date")
admin.site.register(Batch,BatchAdmin)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project','created_by')
    actions = None

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'created_by', None) is None:
            obj.created_by = request.user
        obj.save()
admin.site.register(BatchUserMapping)