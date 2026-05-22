from django.shortcuts import render, redirect
from .models import Producto

def inicio(request):

    if request.method == 'POST':

        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        precio = request.POST['precio']

        Producto.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            precio=precio
        )

        return redirect('/')

    productos = Producto.objects.all()

    return render(request,
        'index.html',
        {
            'productos': productos
        }
    )


def eliminar_producto(request, id):

    producto = Producto.objects.get(id=id)

    producto.delete()

    return redirect('/')


def editar_producto(request, id):

    producto = Producto.objects.get(id=id)

    if request.method == 'POST':

        producto.nombre = request.POST['nombre']

        producto.descripcion = request.POST['descripcion']

        producto.precio = request.POST['precio']

        producto.save()

        return redirect('/')

    productos = Producto.objects.all()

    return render(request,
        'index.html',
        {
            'productos': productos,
            'editar': producto
        }
    )