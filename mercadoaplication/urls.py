from django.conf.urls import url
from django.urls import path
from mercadoaplication.views.public.CategoriasView import *


urlpatterns = [
	path('inicio/',vw_categorias, name='url_categorias'),
]