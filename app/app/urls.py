"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django import views
from django.contrib import admin
from django.urls import path


from app.views.home import index
from app.views.galeria import productos
from app.views.contacto import contacto , formulario_contacto

from app.views.mantenedor_contacto import cargar_contacto

from app.views.cuenta_usuario import crear_usuario, inicio_seccion
from app.views.mantenedor_usuario import cargar_usuarios 

from app.views.kk.ejemplo import calculo


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index) ,
    path('productos/' , productos),
    path('contacto/' , contacto),
    path('contacto/formulario' , formulario_contacto),
    path('mantenedor-contacto', cargar_contacto),
    path('login', inicio_seccion),
    path('login/crear-usuario', crear_usuario),
    path('usuarios',cargar_usuarios),

    path('modulo/',calculo)

]
