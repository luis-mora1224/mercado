"""
    AUTHOR:         luis mora
    CREATION DATE:  01/05/2021
    DESCRIPTION:    Vista de la tabla Categorias del esquema public

    ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

        DATE    ||  MODIFIED_BY ||  DESCRIPTION
    --------------------------------------------------------
                ||              ||  
                ||              ||  
"""
#importar modelos
from mercadoaplication.models.public.Categorias import Categorias

#importar el formulario
from mercadoaplication.forms.public.CategoriasForm import CategoriasForm

from django.shortcuts import render, redirect,get_object_or_404
from django.http.response import HttpResponse,JsonResponse,HttpResponseRedirect
from django.contrib import messages

def vw_categorias(request):
	return render(request,'public/Categorias.html')