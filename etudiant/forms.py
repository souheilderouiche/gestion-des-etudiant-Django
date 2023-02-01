from django.core import validators
from django import forms
from .models import User

class AjoutEtudiant(forms.ModelForm):
    class Meta:
        model = User
        fields = ['nom','prenom','email','password']
        widgets = {
                   'nom':forms.TextInput(attrs={'class':'form-control'}),
                   'prenom':forms.TextInput(attrs={'class':'form-control'}),
                   'email':forms.EmailInput(attrs={'class':'form-control'}),
                   'password':forms.PasswordInput(attrs={'class':'form-control'}),

                  }
