from django.forms import formset_factory
from django import forms 

class ApprovedBank(forms.Form):
    bank_name = forms.CharField(widget = forms.TextInput(attrs={'class': 'form-control'}))
    
ApprovedBankFormSet = formset_factory(
    ApprovedBank,   
    extra=1,    
)

class ProjectLandForm(forms.Form):
    mouza = forms.CharField(widget = forms.TextInput(attrs={'class': 'form-control', 'required': ''}))
    khata_no = forms.CharField(widget = forms.TextInput(attrs={'class': 'form-control', 'required': ''}))
    plot_no = forms.CharField(widget = forms.TextInput(attrs={'class': 'form-control', 'required': ''}))
    kisam = forms.CharField(widget = forms.TextInput(attrs={'class': 'form-control', 'required': ''}))
    area = forms.CharField(widget = forms.TextInput(attrs={'class': 'form-control', 'required': ''}))

ProjectLandFormSet = formset_factory(
    ProjectLandForm,
    extra=1, 
)