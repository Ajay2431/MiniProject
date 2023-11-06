from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User

class ProjectStatus(models.IntegerChoices):
    UNAPPROVED = 0, 'Unapproved'
    SUBMITTED = 1, 'Submitted'
    APPROVED = 2, 'Approved'

class Project(models.Model):
    uuid = models.UUIDField(unique=True, default=uuid4, editable=False)
    project_title = models.CharField(max_length=130)
    email = models.EmailField(blank=True)
    tools = models.CharField(max_length=30, blank=True)
    abstract = models.TextField(blank=True)
    status = models.IntegerField(default=ProjectStatus.SUBMITTED, choices=ProjectStatus.choices)
    created_by = models.CharField(max_length=30)
    """def save(self, *args, **kwargs):
        if self._state.adding is True:
            self.created_by=User.get_username(self.user)
        else:
            self.created_by="achu"
        super().save(*args, **kwargs)  # Call the "real" save() method.
     """
