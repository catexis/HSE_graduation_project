from django import forms
from . import models


class ConfCreateForm(forms.ModelForm):
    
    class Meta:
        model = models.ComputerConf
        fields = '__all__'