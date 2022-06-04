from django.shortcuts import render



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