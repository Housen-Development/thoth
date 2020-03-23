from django import forms


class ExtractionForm(forms.Form):
    inout_date = forms.DateField(label='入出庫日付')
