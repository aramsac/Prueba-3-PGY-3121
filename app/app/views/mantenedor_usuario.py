from wsgiref.util import request_uri
from django.shortcuts import render
from app.models import  Usuario
from app.views.login import authorization

def cargar_usuarios(request):

    if request.method == "GET":
        try:
            
            Usuario.objects.get(pk=request.GET['codigo']).delete()
        except Exception as e:
            print(e)
    
    if request.method == "POST":
        try:           
            usuario             = Usuario.objects.get( pk = request.POST['codigo'])
            usuario.nombre      = request.POST['nombre']
            usuario.email       = request.POST['email']
            usuario.contrasena  = request.POST['contrasena']
            usuario.save( force_update = True )

        except Exception as e:
            print(e)
       
    usuarios = Usuario.objects.all
    return render(request, "mantenedor-usuario.html",{'usuarios':usuarios})