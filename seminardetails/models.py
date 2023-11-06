from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User
from datetime import datetime, date, timedelta
import os
def get_file_path(instance, filename):
    basename,ext = filename.split('.')
    filename = "%s_%s.%s" % (instance.uuid,basename, ext)
    return os.path.join('seminar', filename)

class SeminarStatus(models.IntegerChoices):
    REJECTED = 0, 'Rejected'
    SUBMITTED = 1, 'Submitted'
    APPROVED = 2, 'Approved'

class  Batch(models.Model):
    name=models.CharField(max_length=130, blank=False)
    active=models.BooleanField(default=True)
    deactivation_date=models.DateField(default=datetime.today()+timedelta(days=180))

class BatchUserMapping(models.Model):
    name=models.CharField(max_length=130, blank=False)
    username=models.CharField(max_length=30, blank=False)
    
class Seminar(models.Model):
    batch=models.CharField(max_length=130, blank=False)
    uuid = models.UUIDField(unique=True, default=uuid4, editable=False)
    seminar_title = models.CharField(max_length=130, blank=False)
    paper_link  = models.URLField(max_length=250, blank=False)
    upload_file=models.FileField(upload_to=get_file_path, max_length=254)
    status = models.IntegerField(default=SeminarStatus.SUBMITTED, choices=SeminarStatus.choices)
    created_by = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    approved_by= models.CharField(max_length=30)    
    other_link  = models.URLField(max_length=250, blank=False)
    remarks = models.CharField(max_length=200, default='')