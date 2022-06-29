from itertools import count
from django.http import JsonResponse
from django.shortcuts import render
from app.models import Contacto

from django.core.paginator import Paginator
from django.core import serializers

import math
def cargar_contacto(request):

     
    print('method -> ', request.method)
    if request.method == 'GET':
        try:
            Contacto.objects.get(pk = request.GET['codigo']).delete()
        except Exception as e:
            print(e)

    if request.method == 'POST':
        try:
       
            contacto = Contacto.objects.get(pk = request.POST['codigo'])

            #Actualizando objeto en memoria volatil
            contacto.nombres            = request.POST['nombres']
            contacto.apellido_paterno   = request.POST['apellido_paterno']
            contacto.apellido_materno   = request.POST['apellido_materno']        
            contacto.email              = request.POST['email']         
            contacto.telefono           = request.POST['telefono']           
            contacto.asunto             = request.POST['asunto']
            #Actualizando en la base de datos                      
            contacto.save(force_update=True)
        except Exception as e:
            print(e)
            
    
    #contactos = Contacto.objects.all
    contactos = Contacto.objects.all()
    page      = request.GET.get('page', 1)
    paginator = Paginator( contactos , 2)
    contactos1 = paginator.page(page)

    
    data = {
        'contactos':contactos1,
        'paginator':paginator
    }
    
    modelo_en_json = serializers.serialize("json", contactos)
    data_jason = {"respuesta en ": modelo_en_json}
    #print(" datos en json-->",JsonResponse(data_jason),data_jason)
    print(data['contactos'])

    """"
    page      = request.GET.get('page', 1)
    paginador = Paginator(contactos , 2)
    contactos  = paginador.page(page)
    """
    return render(request, 'mantenedor-contacto.html', { "contactos_json":data_jason , "contactos":data['contactos'],'paginator':data['paginator'] })  

         


