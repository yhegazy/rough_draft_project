from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class RegistrationForm(UserCreationForm):    
    email = forms.EmailField(required=True, widget=forms.EmailInput(
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
   
    class Meta:
        model = User
        fields = (
            'email',
            'is_staff',
            'is_active',
            'is_superuser',
        )