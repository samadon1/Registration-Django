
from .models import Registration
from django import forms
from django.forms import ModelForm

class RegisterationForm(ModelForm):
    class Meta:
        model = Registration
        fields = '__all__' 
 
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Full Name'}),
            'contact':forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Contact: (e.g +233xxxxxxxxx)'}),
            'gender':forms.Select(attrs={'class':'form-control', 'placeholder': 'Gender'}),
            'id_card':forms.Select(attrs={'class':'form-control', 'placeholder': 'ID Card'}),
            'id_number':forms.TextInput(attrs={'class':'form-control', 'placeholder': 'ID Number'}),
            
        }

