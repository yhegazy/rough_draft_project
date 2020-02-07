from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder': 'Username'
        }
    ))

    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class':'form-control',
            'placeholder': 'alphanumeric and @/./+/-/_ only'
        }
    ))

    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class':'form-control',
            'placeholder': 'Confirm password'
        }
    ))
    
    email = forms.EmailField(required=True, widget=forms.EmailInput(
        attrs={
            'class':'form-control',
            'placeholder': 'email@example.com'
        }
    ))

    first_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder': 'Optional'
        }
    ))

    last_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder': 'Optional'
        }
    ))
    
    class Meta:
        model = User
        fields = (
            'username', 
            'password1',
            'password2',
            'email',
            'first_name', 
            'last_name',  
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
        
        return user