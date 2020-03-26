from django import forms

from .models import Location, Parts


class ExtractionForm(forms.Form):
    date_beginning = forms.DateField(initial='', required=False)
    date_end = forms.DateField(initial='', required=False)
    location_code = forms.ModelChoiceField(initial='', queryset=Location.objects.all(), required=False)
    parts_code = forms.ModelChoiceField(initial='', queryset=Parts.objects.all(), required=False)
