from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class RegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder': 'Username'
        }
    ))

    password1 = forms.CharField(label="Password:", widget=forms.PasswordInput(
        attrs={
            'class':'form-control',
            'placeholder': 'alphanumeric and @/./+/-/_ only'
        }
    ))

    password2 = forms.CharField(label="Confirm password:", widget=forms.PasswordInput(
        attrs={
            'class':'form-control',
            'placeholder': 'Verify password'
        }
    ))
    
    email = forms.EmailField(required=True, widget=forms.EmailInput(
        attrs={
            'class':'form-control',
            'placeholder': 'email@example.com'
        }
    ))

    first_name = forms.CharField(required=False, widget=forms.TextInput(
        attrs={
            'class':'form-control',
        }
    ))

    last_name = forms.CharField(required=False, widget=forms.TextInput(
        attrs={
            'class':'form-control',
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

#I may take this out completely 
class EditProfileForm(UserChangeForm):

    """
    TODO: 20200210 - Happy Birthday Ahmed!
    Write a function that brings together all widgets of the same functionality to replace the repitition.
    """

    email = forms.EmailField(required=True, widget=forms.EmailInput(
        attrs={
            'class':'form-control',
        }
    ))

    first_name = forms.CharField(required=False, widget=forms.TextInput(
        attrs={
            'class':'form-control',
        }
    ))

    last_name = forms.CharField(required=False, widget=forms.TextInput(
        attrs={
            'class':'form-control',

        }
    ))
    
    class Meta:
        model = User

        fields = (
            'email',
            'first_name',
            'last_name',
        )

        exclude = ('password1', )
        
