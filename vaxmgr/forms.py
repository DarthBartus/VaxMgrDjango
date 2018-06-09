from django import forms
from .models import Connection, Branch


class ConnectionForm(forms.ModelForm):
    class Meta:
        model = Connection
        fields = ['vaccine', 'branch', 'amount']


class VaccineSearch(forms.Form):
    name = forms.CharField(label='Nazwa szczepionki', max_length=50, required=False)
    illness = forms.CharField(label='Szczepionka przeciw', max_length=100, required=False)
    branch = forms.ModelChoiceField(label='Oddział', queryset=Branch.objects.all(), required=False)
