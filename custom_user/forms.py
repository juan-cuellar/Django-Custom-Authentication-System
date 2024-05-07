from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import CustomUser

class LoginForm(AuthenticationForm):
    #email = forms.EmailField(label='Enter Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Enter Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    

class CustomUserForm(forms.ModelForm):
    '''User registration form in the database
    Variable:
        - password1: pasword
        - password2: password verification
    '''
    

    email = forms.CharField(label='Email', widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter your Email',
            'id': 'email',
            'required': 'required',

        }
    ))


    name = forms.CharField(label='Name', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter your Name',
            'id': 'name',
            'required': 'required',

        }
    ))


    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter your Password',
            'id': 'password1',
            'required': 'required',

        }
    ))
    password2 = forms.CharField(label='Confirmation Password', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Confirm your Password',
            'id': 'password2',
            'required': 'required',

        }
    ))

    class Meta:
        model = CustomUser
        fields = ['email', 'name']
        widget = {
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Email',
                }
            ),
            'name': forms.TimeInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Name',
                }
            )}
        
    def clear_password2(self):
        '''Validation password
            Method that validates that both passwords entered are the same, this before being
            encrypted and saved in the database, returns the valid password.
            1. Excepciones :
            ValidationError-- cuando las contraseñas no son iguales muestra un mensaje de error
        '''

        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError('Password do not Match')
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user