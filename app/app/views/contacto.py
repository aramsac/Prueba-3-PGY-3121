from django.shortcuts import render
from app.models import Contacto

def contacto(request):
    return render(request,'contacto.html')

def formulario_contacto(request):
    print('form de contacto',Contacto)

    if request.method == 'GET':
        print("metoodo get")
        rut = request.GET.get('rut')
        
        print('rut --> {0}'.format(rut))

    elif request.method =='POST':
        print(request.POST.get('rut'),request.GET.get('nombres'))
        run =request.POST.get('rut').replace('-','')
    
        contacto = Contacto()
        contacto.run              = run[:-1]
        contacto.dv               = run[len(run)-1] 
        contacto.nombres          = request.POST.get('nombres')
        contacto.apellido_paterno = request.POST.get('apellido-paterno')
        contacto.apellido_materno = request.POST.get('apellido-materno')
        contacto.email            = request.POST.get('email')
        contacto.telefono         = request.POST.get('telefono')
        contacto.asunto           = request.POST.get('asunto')
        
        contacto.save()
    else:
        print("no envio niusnasnm")
    return render(request,'contacto.html')