from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('project_title', 'email', 'tools', 'abstract')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save Project')) 
class ProjectDeleteForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('project_title', 'email', 'tools', 'abstract')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Delete')) 

class CoordinatorForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('project_title', 'email', 'tools', 'abstract','status')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Update Status')) 
