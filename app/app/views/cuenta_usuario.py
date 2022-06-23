from django.shortcuts import render
from app.models import Usuario

def inicio_seccion(request):
    return render(request,'seccion.html')

def crear_usuario(request):
    print('form de creacion cuenta', Usuario)

    if request.method == 'GET':
        print("metoodo get")

    elif request.method =='POST':
        print(request.POST.get('nombre'),request.POST.get('contrasena'))
        usuario = Usuario()
        usuario.nombre         = request.POST.get('nombre')
        usuario.contrasena     = request.POST.get('contrasena')
        usuario.email          = request.POST.get('email')
        
        usuario.save()
        print(usuario)
    else:
        print("no envio niusnasnm")
    return render(request,'seccion.html')