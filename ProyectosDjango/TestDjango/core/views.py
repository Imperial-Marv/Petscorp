from django.shortcuts import render



def home(request):
    contexto={"nombre":"Marcel"}
    return render(request,'core/index0.html',contexto)