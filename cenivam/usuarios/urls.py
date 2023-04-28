from django.urls import path
from. import views

urlpatterns = [ #Lo primero del path es el url 
                #lo segundo la referencia con la vista 
                #Lo tercero el nombre que usaremos para llamarlo en otro html :)
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('usuarios', views.usuarios, name='usuarios'),
    path('usuarios/crear', views.crear_usuarios, name='crear'),
]