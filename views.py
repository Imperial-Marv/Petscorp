from django.shortcuts import render
from .models import Producto


def home(request):
    contexto={"nombre":"Marcel"}
    return render(request,'core/index0.html',contexto)

def home1(request):

    return render(request,'core/index.html')   

def us(request):

    return render(request,'core/quienes_somos.html')  

def don(request):

    return render(request,'core/donaciones.html')  

def perro (request):

    return render(request,'core/perro.html')  

def gato(request):

    return render(request,'core/gato.html')  

def login(request):

    return render(request,'core/login.html')  

def creacuenta(request):

    return render(request,'core/creausuario.html')   

def clima(request):

    return render(request,'core/climadetalles.html')   

def carrito(request):

    return render(request,'core/carrito.html')       

def admin(request):

    return render(request,'http://127.0.0.1:8000/admin/login/?next=/admin/')       


def gato1(request):

    return render(request,'core/gato1.html')  
    


def producto (request):
    producto_list = Producto.objects.all()
    return render (request,'core/gato1.html',
    {'producto_list': producto_list})


# def product_detail_view(request):
#    obj = producto.objects.all()
#    context = { 'allobject' : obj }
#    return render(request, "core/gato1.htm", context)

# def gato1(request):
#     producto = Producto.objects.all()

#     datos = {
#         'Productos': producto
#     }
#     return render(request,'core/gato1.html',datos)
