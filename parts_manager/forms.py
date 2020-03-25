from django import forms

from .models import Location, Parts


class ExtractionForm(forms.Form):
    date_beginning = forms.DateField(required=False)
    date_end = forms.DateField(required=False)
    location_code = forms.ModelChoiceField(queryset=Location.objects.all(), required=False)
    parts_code = forms.ModelChoiceField(queryset=Parts.objects.all(), required=False)
