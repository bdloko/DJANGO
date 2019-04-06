from django import forms
from django.db import models
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User
from provider.models import Provider
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import authenticate

class Email(forms.EmailField): 
    def clean(self, value):
        super(Email, self).clean(value)
        try:
            User.objects.get(email=value)
            raise forms.ValidationError("This email is already registered. Use the 'forgot password' link on the login page")
        except User.DoesNotExist:
            return value

class RegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        for password1 in ['password1',]:
            self.fields[password1].help_text = "Your password can't be too similar to your other personal information, and must contain at least 8 characters."

    email = Email()

    class Meta:
        model = User
        fields = (
            'email',
            'password1',
            'password2',
        )
        
    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.password2 = self.cleaned_data['password1']
        user.password1 = self.cleaned_data['password2']
        user.email = self.cleaned_data['email']
        user.username = user.email

        if commit:
            user.save()

        return user

class ChangePass(PasswordChangeForm):
    
    def __init__(self, *args, **kwargs):
        super(ChangePass, self).__init__(*args, **kwargs)
        for password1 in ['new_password1']:
            self.fields[password1].help_text = "Your password must contain at least 8 characters.Your password can't be entirely numeric"
    
        class Meta:
            model = User
            fields = (
                'old_password',
                'new_password1',
                'new_password2',
        )

class LoginForm(forms.Form):

    email = forms.EmailField(max_length=50, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        user = authenticate(username=email, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError("Sorry, that login was invalid. Please try again.")
        return self.cleaned_data

    def login(self, request):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        user = authenticate(username=email, password=password)
        return user

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        for password1 in ['password',]:
            self.fields[password1].input = False
        for email in ['email']:
            self.fields[email].help_text = False

    class Meta:
        model = User
        fields = (
            'email',
            'password1',
        )

class ProviderForm(forms.ModelForm):

    class Meta:
        model = Provider
        fields = (
            'company_name',
            'address_line_1',
            'address_line_2',
            'city',
            'postal_code',
            'registration_no',
            'email_address',
            'website',
            'telephone',
            'logo',
            'description',
        )