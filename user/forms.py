from django import forms
from .models import User


class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['email','password','phone',]

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('This Email already exist!!')
        return email
    
class ProfileForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ['phone','bio','image']
