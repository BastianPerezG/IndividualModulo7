from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views.generic import TemplateView, DeleteView
from django.contrib.auth import authenticate, login
from tareasApp.form import FormularioLogin, FormularioRegistro, FormularioTareas
from tareasApp.models import Tarea
from django.urls import reverse_lazy
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
        tareas = Tarea.objects.all().order_by('-fecha_vencimiento')
        context = {
            "titulo": title,
            "primer_nombre": primer_nombre,
            "primer_apellido": primer_apellido,
            "tareas" : tareas
        }
        return render(request, self.template_name, context)
    

class TareaCreateView(TemplateView):
    template_name = 'agregar_tarea.html'
    def get(self, request, *args, **kwargs):
        title = "Crear Tarea"
        context = {
            "titulo": title
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        title = "Crear Tarea"
        titulo = request.POST.get('titulo')
        descripcion = request.POST.get('descripcion')
        fecha = request.POST.get('fecha')
        tarea = Tarea(titulo=titulo, descripcion=descripcion, fecha=fecha)
        tarea.save()
        context = {
            "titulo": title
        }
        return render(request, self.template_name, context)
    
class TareaUpdateView(TemplateView):
    template_name = 'editar_tarea.html'
    def get(self, request, *args, **kwargs):
        idtarea = kwargs['idtarea']
        try:
            tarea = Tarea.objects.get(id=idtarea)
        except Tarea.DoesNotExist:
            return render(request, 'elemento_no_existe.html')
        context = {
            'form': FormularioTareas(instance=tarea),
            'title': 'Editar producto',
            'idtarea': idtarea
        }
        return render(request, self.template_name, context)

    def post(self, request, idtarea, *args, **kwargs):
        tarea = get_object_or_404(Tarea, id=idtarea)
        form = FormularioTareas(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            request.session['mensajes'] = {'enviado': True, 'resultado': 'Se ha actualizado el estado de la tarea'}
            return redirect('tareas')
        return self.render_to_response(self.get_context_data())             

class TareaDeleteView(DeleteView):
    template_name = 'eliminar_tarea.html'
    model = Tarea
    success_url = reverse_lazy('tareas')