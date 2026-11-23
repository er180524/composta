from django.shortcuts import render
from .models import Guia, Residuo


def inicio(request):
    contexto = {
        'verdes': Residuo.objects.filter(categoria='VERDE'),
        'marrones': Residuo.objects.filter(categoria='MARRON'),
        'prohibidos': Residuo.objects.filter(categoria='PROHIBIDO'),
        'guias': Guia.objects.all().order_by('-fecha_publicacion'),
    }
    return render(request, 'composta/inicio.html', contexto)