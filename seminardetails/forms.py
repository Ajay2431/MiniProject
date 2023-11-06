from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Seminar
class ModelAllDisabledFormMixin(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        '''
        This mixin to ModelForm disables all fields. Useful to have detail view based on model
        '''
        super().__init__(*args, **kwargs)
        form_fields = self.fields
        for key in form_fields.keys():
            if key!="status":   
                form_fields[key].disabled = True
class SeminarForm(forms.ModelForm):
    class Meta:
        model = Seminar
        fields = ('seminar_title', 'paper_link', 'upload_file')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save Seminar')) 
class SeminarDeleteForm(forms.ModelForm):
    class Meta:
        model = Seminar
        fields = ('seminar_title', 'paper_link', 'upload_file')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Delete')) 

class CoordinatorForm(ModelAllDisabledFormMixin,forms.ModelForm):
    class Meta:
        model = Seminar
        fields = ('seminar_title', 'paper_link', 'upload_file','status')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Update Status')) 
