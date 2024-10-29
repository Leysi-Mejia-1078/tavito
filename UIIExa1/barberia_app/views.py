from django.shortcuts import render
from .models import Local

# Create your views here.

def inicio_vista(request):
    ListadoLocales=Local.objects.all()
    return render(request,"gestionarLocal.html",{"loslocales":ListadoLocales})