from django.shortcuts import render, HttpResponse, redirect
from .models import *

def principal_libros(request):
    context = {
        'libros': Book.objects.all()
    }
    return render(request, 'libros_1.html', context)

def principal_autores(request):
    context = {
        'autores': Author.objects.all()
    }
    return render(request, 'autor_1.html', context)

def crearlibro(request):
    crear_libro = Book.objects.create(
        title = request.POST['titulo'],
        desc = request.POST['description'])
    return redirect("/")

def crearautor(request):
    crear_autor = Author.objects.create(
        first_name = request.POST['nombre'],
        last_name = request.POST['apellido'],
        notas = request.POST['notas'])
    return redirect("/authors")
    
def rutasl(request, num):
    context = {
        'libro': Book.objects.get(id=num),
        'autores': Book.objects.get(id=num).authors.all(),
        'autores1': Author.objects.all()
    }
    return render(request, 'libros_2.html', context)

def rutasa(request, num):
    context = {
        'autor': Author.objects.get(id=num),
        'libros': Author.objects.get(id=num).books.all(),
        'libros1': Book.objects.all()
    }
    return render(request, 'autor_2.html', context)

def asociar_autor(request):
    libro_id= request.POST['id_libro']
    id_autor = request.POST['autores']
    autor = Author.objects.get(id=id_autor)
    libro = Book.objects.get(id=libro_id)
    autor.books.add(libro)
    return redirect(f"/books/{libro_id}")

def asociar_libro(request):
    libros_1 = request.POST['libros']
    autor = request.POST['id_autor']
    libro = Book.objects.get(id=libros_1)
    autor_1 = Author.objects.get(id = autor)
    libro.authors.add(autor_1)
    return redirect(f"/authors/authors/{autor}")