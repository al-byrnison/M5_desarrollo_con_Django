from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render(
        request,'app_ex/inicio.html',
        context={'titulo':'Titulo generado por Django','texto':'Texto del ejercicio 1, modulo 5'}
        )