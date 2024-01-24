from django import forms
from .models import DashboardData

class DashboardDataForm(forms.ModelForm):
    class Meta:
        model = DashboardData
        fields = '__all__'
        
    Intensity = forms.TextInput(attrs={'class': 'form-control'})
    Likelihood = forms.TextInput(attrs={'class': 'form-control'})
    Relevance = forms.TextInput(attrs={'class': 'form-control'})
    Year = forms.TextInput(attrs={'class': 'form-control'})
    Country = forms.TextInput(attrs={'class': 'form-control'})
    Topics = forms.TextInput(attrs={'class': 'form-control'})
    Region = forms.TextInput(attrs={'class': 'form-control'})
    City = forms.TextInput(attrs={'class': 'form-control'})