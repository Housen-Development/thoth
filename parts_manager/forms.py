from django import forms

from .models import PartsInOut


class ExtractionForm(forms.Form):
    keyword = forms.CharField(initial='', label='キーワード', required=False)
