from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views.generic import TemplateView, DeleteView, View
from django.contrib.auth import authenticate, login
from tareasApp.form import FormularioLogin, FormularioRegistro, FormularioTareas, FormularioEditarTareas, FormularioObservaciones
from tareasApp.models import Tarea, Etiqueta, Estado
from django.urls import reverse_lazy
from django.http import HttpResponse
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
        id_busqueda = request.session.get('id_busqueda', 0)
        if id_busqueda == 0:
            tareas = Tarea.objects.filter(usuario_id=request.user.id).order_by('fecha_vencimiento')
        else:
            tareas = Tarea.objects.filter(usuario_id=request.user.id, etiqueta_id=id_busqueda).order_by('fecha_vencimiento')
        request.session.pop('id_busqueda', None)

        tareas_con_prioridad = []  # Lista para almacenar las tareas con información de prioridad
        for tarea in tareas:
            tarea_info = {
                'tarea': tarea,
                'prioridad': tarea.prioridad.nombre  # Accede al nombre de la prioridad
            }
            tareas_con_prioridad.append(tarea_info)

        context = {
            'titulo': 'Visualizador de Tareas',
            'primer_nombre': request.user.first_name,
            'primer_apellido': request.user.last_name,
            'tareas': tareas_con_prioridad,  # Pasamos la lista de tareas con prioridad al contexto
            'etiquetas': Etiqueta.objects.all().order_by('id'),
            'estados': Estado.objects.all().order_by('id'),
            'mensajes': request.session.get('mensajes', None),
        }
        request.session.pop('mensajes', None)
        return render(request, self.template_name, context)


    
class TareaDetailView(TemplateView):
    template_name = 'detalle_tarea.html'

    def get(self, request, pk, *args, **kwargs):
        title = "Detalle de Tarea"
        try:
            tarea = Tarea.objects.get(id=pk)
        except Tarea.DoesNotExist:
            return render(request, 'elemento_no_existe.html')
        form_observacion = FormularioObservaciones()
        context = {
            "titulo": title,
            "tarea": tarea,
            "form_observacion": form_observacion,
            "prioridad": tarea.prioridad.nombre  
        }
        return render(request, self.template_name, context)

    def post(self, request, pk, *args, **kwargs):
        tarea = get_object_or_404(Tarea, id=pk)
        form_observacion = FormularioObservaciones(request.POST)
        if form_observacion.is_valid():
            observacion = form_observacion.cleaned_data['observaciones']
            tarea.observaciones = observacion
            tarea.save()
            return redirect('tarea', pk=pk)
        else:
            context = {
                "titulo": "Detalle de Tarea",
                "tarea": tarea,
                "form_observacion": form_observacion,
                "prioridad": tarea.id_prioridad  # Agrega la prioridad al contexto
            }
            return render(request, self.template_name, context)

class TareaCreateView(View):
    template_name = 'agregar_tarea.html'

    def get(self, request, *args, **kwargs):
        title = "Crear Tarea"
        context = {
            "titulo": title,
            'form': FormularioTareas(),
            'accion': 'crear'
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = FormularioTareas(request.POST, request.FILES)
        if form.is_valid():
            tarea = form.save(commit=False)
            tarea.usuario = form.cleaned_data['usuario_destinatario']
            tarea.save()
            request.session['mensajes'] = {'enviado': True, 'resultado': 'Has creado la tarea exitosamente'}
            return redirect('tareas')
        else:
            mensajes = {'enviado': False, 'resultado': form.errors}
        context = {
            'title': 'Crear nueva Tarea',
            'mensajes': mensajes,
            'form': form,
        }
        return render(request, self.template_name, context)
    

class TareaUpdateView(View):
    template_name = 'agregar_tarea.html'

    def get(self, request, pk=None, *args, **kwargs):
        tarea = get_object_or_404(Tarea, id=pk) if pk is not None else None
        form = FormularioEditarTareas(instance=tarea)
        accion = 'editar' if tarea else 'crear'
        context = {
            'form': form,
            'title': f'{accion.capitalize()} tarea',
            'accion': accion,
            'tarea': tarea
        }
        return render(request, self.template_name, context)

    def post(self, request, pk=None, *args, **kwargs):
        tarea = get_object_or_404(Tarea, id=pk) if pk is not None else None
        form = FormularioEditarTareas(request.POST, instance=tarea)

        if form.is_valid():
            tarea = form.save()
            request.session['mensajes'] = {'enviado': True, 'resultado': 'Se ha actualizado el estado de la tarea'}
            return redirect(reverse('tarea', kwargs={'pk': tarea.pk}))

        accion = 'editar' if tarea else 'crear'
        context = {
            'form': form,
            'title': f'{accion.capitalize()} tarea',
            'accion': accion,
            'tarea': tarea
        }
        return render(request, self.template_name, context)

class TareaDeleteView(DeleteView):
    template_name = 'eliminar_tarea.html'
    model = Tarea
    success_url = reverse_lazy('tareas')

class CompletarTareaView(View):
    def get(self, request, pk, *args, **kwargs):
        tarea = get_object_or_404(Tarea, id=pk)
        estado_completada = Estado.objects.get(nombre='Completada')
        tarea.estado = estado_completada
        tarea.save()
        return redirect('tareas')