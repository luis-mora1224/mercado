from django.conf.urls import url
from django.urls import path
from mercadoaplication.views.public.InicioView import *
from mercadoaplication.views.public.CategoriasView import *


urlpatterns = [
	path('inicio/',vw_Inicio, name='url_inicio'),

	path('categoria/',vw_categorias, name='url_categoria'),
	path('categoria/new',vw_categorias_new, name='url_categoria_new'),
    path('categoria/delete/<pk>', vw_categorias_delete, name='url_categoria_delete'),
    path('categoria/articulo',vw_categorias_Articulos_hogar, name='url_Articulos_hogar'),
    path('categoria/actualizar/<pk>', vw_categorias_actualizar, name='url_categoria_actualizar'),
]