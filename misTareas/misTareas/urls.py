"""
URL configuration for misTareas project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required
from tareasApp.views import LandingPageView, RegistroView, IngresoView, TareasView, TareasCreateView, TareasDetailView, TareasUpdateView, TareasDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LandingPageView.as_view(), name='TaskWise'),
    path("login/", IngresoView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(next_page='TaskWise'), name='logout'),
    path("registrarse", RegistroView.as_view(), name="registrarse"),
    path("tareas", login_required(TareasView.as_view()), name="tareas"),
    path("tareas/nueva", login_required(TareasCreateView.as_view()), name="agregar_tarea"),
    path("tareas/<int:pk>", login_required(TareasDetailView.as_view()), name="tarea"),
    path("tareas/<int:pk>/editar", login_required(TareasUpdateView.as_view()), name="editar_tarea"),
    path("tareas/<int:pk>/eliminar", login_required(TareasDeleteView.as_view()), name="eliminar_tarea"),
]