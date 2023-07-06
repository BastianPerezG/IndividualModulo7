from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from tareasApp.models import Etiqueta, Estado

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

class FormularioTareas(forms.Form):
    opciones_estado = Estado.objects.all().values_list('id', 'nombre').order_by('nombre')
    OPCIONES_ESTADO = [(1, 'Pendiente'), (2, 'En Progreso'), (3, 'Completada')]
    opciones_etiqueta = Etiqueta.objects.all().values_list('id', 'nombre').order_by('nombre')
    OPCIONES_ETIQUETA = [(1, 'Trabajo'), (2, 'Hogar'), (3, 'Estudio')]

    id = forms.CharField(widget=forms.HiddenInput(), required=False)
    titulo = forms.CharField(label="Titulo", required=True,
                            error_messages={
                                'required': 'El titulo es requerido'},
                            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titulo', 'type': 'text'}))
    fecha = forms.DateField(label="FechaVencimiento", required=True,
                            error_messages={
                                'required': 'La fecha de vencimiento es requerida'},
                            widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Fecha', 'type': 'date'}),
                            help_text='Ingrese la fecha de vencimiento de la tarea')
    estado = forms.ChoiceField(choices=OPCIONES_ESTADO, required=True,
                                error_messages={'required': 'El estado de la tarea es requerida'},
                                widget=forms.Select(attrs={'class': 'form-control'}),
                                help_text='Seleccione el estado de la tarea')
    forma_pago = forms.ChoiceField(choices=OPCIONES_ETIQUETA, required=True,
                                    error_messages={'required': 'La etiqueta es requerida'},
                                    widget=forms.Select(attrs={'class': 'form-control'}),
                                    help_text='Seleccione la etiqueta de la tarea')
