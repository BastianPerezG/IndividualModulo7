from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login
from tareasApp.form import FormularioLogin, FormularioRegistro

# Create your views here.

class LandingPageView(TemplateView):
    template_name = "landing_page.html"
    def get(self, request, *args, **kwargs):
        title = "TaskWise"
        return render(request, self.template_name, {'titulo': title})
    
class IngresoView(TemplateView):
    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        title = "Ingreso"
        form = FormularioLogin()
        context = {
            'titulo': title,
            'form': form
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = FormularioLogin(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('tareas')
                else:
                    form.add_error('username', 'Credenciales incorrectas')
        return render(request, self.template_name, { "form": form })
        
class RegistroView(TemplateView):
    template_name = 'registro.html'

    def get(self, request, *args, **kwargs):
        form = FormularioRegistro()
        title = "Registro de Usuario"
        context = {
            "form": form,
            "titulo": title
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = FormularioRegistro(request.POST, request.FILES)
        title = "Registro de Usuario"
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            user.save()
            mensajes = {"enviado": True, "resultado": "Has creado un nuevo usuario exitosamente"}
        else:
            mensajes = {"enviado": False, "resultado": form.errors}
        context ={
            "form": form,
            "mensajes": mensajes,
            "titulo": title
        }
        return render(request, self.template_name, context)
    
class TareasView(TemplateView):
    template_name = 'tareas.html'
    def get(self, request, *args, **kwargs):
        title = "Visualizador de Tareas"
        primer_nombre = request.user.first_name
        primer_apellido = request.user.last_name
        context = {
            "titulo": title,
            "primer_nombre": primer_nombre,
            "primer_apellido": primer_apellido
        }
        return render(request, self.template_name, context)