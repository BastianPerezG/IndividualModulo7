from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from tareasApp.models import Etiqueta, Estado, Tarea

class FormularioLogin(forms.Form):
    username = forms.CharField(label='NombreUsuario', required=True,
                                max_length=30, min_length=5,
                                error_messages={
                                    'required': 'El nombre de usuario es obligatorio',
                                    'max_length': 'El usuario no puede superar los 30 caracteres',
                                    'min_length': 'El usuario debe tener al menos 5 caracteres'
                                },
                                widget=forms.TextInput(attrs={
                                    'placeholder': 'Ingrese su nombre de usuario',
                                    'class': 'form-control'
                                })
                                )
    password = forms.CharField(label='Contraseña', required=True,
                                max_length=30, min_length=1,
                                error_messages={
                                    'required': 'La contraseña es obligatoria',
                                    'max_length': 'La contraseña no puede superar los 30 caracteres',
                                    'min_length': 'La contraseña debe tener al menos 1 caracter'
                                },
                                widget=forms.PasswordInput(attrs={
                                    'placeholder': 'Ingrese su contraseña',
                                    'class': 'form-control'
                                })
                                )
    
class FormularioRegistro(UserCreationForm):
    username = forms.CharField(label='NombreUsuario', required=True,
                                max_length=30, min_length=5,
                                error_messages={
                                    'required': 'El nombre de usuario es obligatorio',
                                    'max_length': 'El usuario no puede superar los 30 caracteres',
                                    'min_length': 'El usuario debe tener al menos 5 caracteres'
                                },
                                widget=forms.TextInput(attrs={
                                    'placeholder': 'Ingrese su nombre de usuario',
                                    'class': 'form-control'
                                })
                                )
    first_name = forms.CharField            (label="Nombre", required = True, max_length=30,
                                        error_messages={
                                            'required': 'El nombre del usuario es Obligatorio',
                                            'max_length': 'El nombre debe tener como maximo 30 caracteres',
                                        },
                                        widget= forms.TextInput(attrs={
                                            'placeholder': 'Ingrese el nombre del usuario',
                                            'class':'form-control'}),
                                        )

    last_name = forms.CharField          (label="Apellido", required = True, max_length=30,
                                        error_messages={
                                            'required': 'El apellido del usuario es obligatorio',
                                            'max_length': 'El apellido debe tener como maximo 30 caracteres',
                                        },
                                        widget= forms.TextInput(attrs={
                                            'placeholder': 'Ingrese el apellido del usuario',
                                            'class':'form-control'}),
                                        )
    email = forms.EmailField    (label="Email", required = True, max_length=30,
                                    error_messages={
                                            'required': 'Tiene que indicar el email del usuario',
                                            'max_length': 'La dirección de email tiene más de 30 caracteres',
                                        },
                                    widget= forms.TextInput(attrs={
                                            'placeholder':'Ingrese su correo electrónico',
                                            'class':'form-control',
                                            'type':'email'})
                                    )
    password1 = forms.CharField(label='Contraseña', required=True,
                                max_length=30, min_length=1,
                                error_messages={
                                    'required': 'La contraseña es obligatoria',
                                    'max_length': 'La contraseña no puede superar los 30 caracteres'
                                    },
                                widget=forms.PasswordInput(attrs={
                                    'placeholder': 'Ingrese su contraseña',
                                    'class': 'form-control'
                                })
                                )
    password2 = forms.CharField(label='Contraseña', required=True,
                                max_length=30, min_length=1,
                                error_messages={
                                    'required': 'La contraseña es obligatoria',
                                    'max_length': 'La contraseña no puede superar los 30 caracteres'
                                    },
                                widget=forms.PasswordInput(attrs={
                                    'placeholder': 'Ingrese su contraseña',
                                    'class': 'form-control'
                                })
                                )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'first_name', 'last_name','email', 'password1', 'password2')

class FormularioTareas(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['titulo', 'fecha_vencimiento', 'estado', 'descripcion', 'etiqueta']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titulo', 'type': 'text'}),
            'fecha': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Fecha', 'type': 'date'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Descripcion', 'type': 'text'}),
            'etiqueta': forms.Select(attrs={'class': 'form-control'})
        }
        labels = {
            'titulo': 'Titulo',
            'fecha': 'Fecha de Vencimiento',
            'estado': 'Estado',
            'descripcion': 'Descripcion',
            'etiqueta': 'Etiqueta',
        }
        error_messages = {
            'titulo': {'required': 'El título es requerido'},
            'fecha': {'required': 'La fecha de vencimiento es requerida'},
            'estado': {'required': 'El estado de la tarea es requerido'},
            'descripcion': {'required': 'La descripción es requerida'},
            'etiqueta': {'required': 'La etiqueta es requerida'}    
        }
                                
    

class FormularioEditarTareas(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['titulo', 'fecha_vencimiento','descripcion', 'estado', 'etiqueta']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titulo', 'type': 'text'}),
            'fecha_vencimiento': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Fecha', 'type': 'date'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Descripcion', 'type': 'text'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
            'etiqueta': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'titulo': 'Titulo',
            'fecha_vencmiento': 'Fecha de Vencimiento',
            'descripcion': 'Descripcion',
            'estado': 'Estado',
            'etiqueta': 'Etiqueta',
        }
        error_messages = {
            'titulo': {'required': 'El título es requerido'},
            'fecha_vencimiento': {'required': 'La fecha de vencimiento es requerida'},
            'descripcion': {'required': 'La descripción es requerida'},
            'estado': {'required': 'El estado de la tarea es requerido'},
            'etiqueta': {'required': 'La etiqueta es requerida'},
        }