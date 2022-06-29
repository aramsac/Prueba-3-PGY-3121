from django.shortcuts import render


from app.modulo1.calcular import calcular  

def calculo(request):
    p = calcular(10,20)
    return render(request,'modulo.html',{'a':p})