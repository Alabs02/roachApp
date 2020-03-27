from django import forms
from . import models

class CreateReport(forms.ModelForm):
    class Meta:
        model = models.Report
        fields = ['title', 'slug', 'content', 'number', 'thumb']