from django.shortcuts import render
from .carro import Carro
from tienda.models import Producto
from django.shortcuts import redirect
# Create your views here.

def agregarProducto(request, producto_id):
    carro=Carro(request)
    producto=Producto.objects.get(id=producto_id)
    carro.agregar(producto=producto)
    return redirect("tienda")


def eliminarProducto(request, producto_id):
    carro=Carro(request)
    producto=Producto.objects.get(id=producto_id)
    carro.eliminar(producto=producto)
    return redirect("tienda")

def restarProducto(request, producto_id):
    carro=Carro(request)
    producto=Producto.objects.get(id=producto_id)
    carro.restar_producto(producto=producto)
    return redirect("tienda")

def limpiarCarro(request):
    carro=Carro(request)
    carro.limpiar_carro()
    return redirect("tienda")