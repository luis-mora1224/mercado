from django.conf.urls import url
from django.urls import path
from mercadoaplication.views.public.InicioView import *
from mercadoaplication.views.public.CategoriasView import *


urlpatterns = [
	path('inicio/',vw_Inicio, name='url_inicio'),

	path('categoria/',vw_categorias, name='url_categoria'),
	path('categoria/new',vw_categorias_new, name='url_categoria_new'),
]