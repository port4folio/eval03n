from django.shortcuts import render
from librosapp.models import Libro
from django.shortcuts import render,redirect
from librosapp.forms import LibroForm

from . import forms

def  index(request):
    form = forms.LibroForm()
    if request.method == 'POST':
        form = forms.LibroForm(request.POST)
        if form.is_valid():
            print("Libro guardado")
            print(Formulario Ok)
            form.save()
            return redirect('index')
    data = {'form': form}
    return render(request, 'librosapp/index.html', data)

def lista_libros(request):
    libros = Libro.objects.all()
    data = {'libros': libros}
    return render(request, 'librosapp/lista_libros.html', data)

def editar_libro(request, id):
    libro = Libro.objects.get(id=id)
    form = forms.LibroForm(instance=libro)
    if request.method == 'POST':
        form = forms.LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            return redirect('lista_libros')
    data = {'form': form}
    return render(request, 'librosapp/editar_libro.html', data)

def eliminar_libro(request, id):
    libro = Libro.objects.get(id=id)
    libro.delete()
    return redirect('lista_libros')

def buscar_libro(request):
    if request.method == 'POST':
        titulo = request.POST['titulo']
        libros = Libro.objects.filter(titulo__icontains=titulo)
        data = {'libros': libros}
        return render(request, 'librosapp/lista_libros.html', data)
    return render(request, 'librosapp/buscar_libro.html') 

def agregar_libro(request):
    form = forms.LibroForm()
    if request.method == 'POST':
        form = forms.LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_libros')
    data = {'form': form}
    return render(request, 'librosapp/agregar_libro.html', data)
    

# Create your views here.
