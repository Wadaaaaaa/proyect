from django.shortcuts import render, redirect, get_object_or_404
from .models  import Aprendiz, Calificaciones, Competencias
from .forms import AprendizForm

# Create your views here.

def base(request):
    return render(request, 'base.html')

def aprendiz(request):
    aprendiz = Aprendiz.objects.all()
    return render(request, 'aprendiz.html', {'aprendiz': aprendiz})

def agregar(request):
    formulario = AprendizForm(request.POST or None) 
    if formulario.is_valid(): 
        formulario.save() 
        return redirect('aprendiz') 
    return render(request, 'agregar.html', {'formulario': formulario}) 

def eliminar(request, id):
    aprendiz = get_object_or_404(Aprendiz, id=id)
    aprendiz.delete()
    return redirect('aprendiz')


def editar(request, id): 
    aprendiz = get_object_or_404(Aprendiz, id=id)
    
    if request.method == 'POST':
        formulario = AprendizForm(request.POST, instance=aprendiz)
        if formulario.is_valid():
            formulario.save()
            return redirect('aprendiz')
    else:
        formulario= AprendizForm(instance=aprendiz)
    return render(request, 'editar.html', {'formulario': formulario})

def cali(request):
    cali = Calificaciones.objects.all()
    return render(request, 'cali.html', {'cali': cali})

def compe(request):
    compe = Competencias.objects.all()
    return render(request, 'compe.html', {'compe': compe})
