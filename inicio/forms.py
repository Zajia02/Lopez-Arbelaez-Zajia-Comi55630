from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CamperaForm(forms.Form):
    talle = forms.CharField(max_length=50, required=True)
    color1= forms.CharField(max_length=50, required=True)
    color2 = forms.CharField(max_length=50, required=True)
    modelo = forms.CharField(max_length=50, required=True)
    
class ChalecoForm(forms.Form):
    talle = forms.CharField(max_length=50, required=True)
    color1= forms.CharField(max_length=50, required=True)
    color2 = forms.CharField(max_length=50, required=True)
    modelo = forms.CharField(max_length=50, required=True)
    
class ChaparrerasForm(forms.Form):
    talle = forms.IntegerField(required=True)
    color1= forms.CharField(max_length=50, required=True)
    color2 = forms.CharField(max_length=50, required=True)
    modelo = forms.CharField(max_length=50, required=True)
    
class GuantesForm(forms.Form):
    talle = forms.IntegerField(required=True)
    color1= forms.CharField(max_length=50, required=True)
    color2 = forms.CharField(max_length=50, required=True)
    modelo = forms.CharField(max_length=50, required=True)
    
class PantalonForm(forms.Form):
    talle = forms.IntegerField(required=True)
    color1= forms.CharField(max_length=50, required=True)
    color2 = forms.CharField(max_length=50, required=True)
    modelo = forms.CharField(max_length=50, required=True)            
    
class RegistroUsuariosForm(UserCreationForm):      
    email = forms.EmailField(label="Email de Usuario")
    password1 = forms.CharField(label="Contraseña", widget= forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contraseña", widget= forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']   
        
class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Email de Usuario")
    password1 = forms.CharField(label="Contraseña", widget= forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contraseña", widget= forms.PasswordInput) 
    first_name = forms.CharField(label="Nombre/s", max_length=50, required=False)   
    last_name = forms.CharField(label="Apellido/s", max_length=50, required=False)   

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'first_name', 'last_name'] 
        
class AvatarFormulario(forms.Form):
    imagen = forms.ImageField(required=True)                