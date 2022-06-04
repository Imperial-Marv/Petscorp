from django.urls import path
from .views  import creacuenta, don, home, perro,us,gato,login,creacuenta,home1,clima

urlpatterns = [
    path('',home,name="home"),
    path('quienes-somos',us,name="us"),
    path('Donations',don,name="don"),
    path('Perros',perro,name="perro"),
    path('Gatos',gato,name="gato"),
    path('Login',login,name="login"),
    path('creacuenta',creacuenta,name="creacuenta"),
    path('Home1',home1,name="home1"),
    path('GeoClima',clima,name="clima")

]