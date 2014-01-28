from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from models import apiuser

class newApiUser(ModelForm):

    class Meta:
        
        model = apiuser
        fields = ('firstname', 'lastname', 'institute', 'email')                  

        def clean_firstname(self):
            if 'firstname' in self.cleaned_data:
                firstname = self.cleaned_data['firstname']
                return firstname
            raise forms.ValidationError('Please enter a name')
        def clean_lastname(self):
            if 'lastname' in self.cleaned_data:
                lastname = self.cleaned_data['lastname']
                return lastname
            raise forms.ValidationError('Please enter a name')
        def clean_email(self):
            if 'email' in self.cleaned_data:
                email = self.cleaned_data['email']
                return email
            raise forms.ValidationError('Please enter a valid email')
        def clean_institute(self):
            if 'institute' in self.cleaned_data:
                institute = self.cleaned_data['institute']
                return institute
            raise forms.ValidationError('Please enter the name of your Institute')
