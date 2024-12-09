from django import forms
from .models import CustomUser

class UserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'name', 'image', 'phone', 'password' ]
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your username'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter your phone number'}),
        }
        
    def check_email(self):
         cleaned_data = super().clean()
         if CustomUser.objects.filter(email=form.cleaned_data.get('emal ')).exists():
             raise form.ValidationError("User already Exists")
         return cleaned_data
     
    def check_username(self):
         cleaned_data = super().clean()
         if CustomUser.objects.filter(username=form.cleaned_data.get('username')).exists():
             raise form.ValidationError("User already Exists")
         return cleaned_data
# 