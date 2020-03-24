from django import forms

from .models import PartsInOut


class PartsInOutForm(forms.ModelForm):
    class Meta:
        model = PartsInOut
        fields = ['location', 'parts', 'warehousing', 'shipping']
