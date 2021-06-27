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
from mercadoaplication.models.Categorias import Categorias

#importar el formulario
from mercadoaplication.forms.public.CategoriasForm import CategoriasForm

from django.shortcuts import render, redirect,get_object_or_404
from django.http.response import HttpResponse,JsonResponse,HttpResponseRedirect
from django.contrib import messages

def vw_categorias(request):
	form = CategoriasForm()
	categorias = Categorias.objects.all();
	return render(request, 'public/categoria.html', {'form':form, 'categorias':categorias})

def vw_categorias_new(request):
	if request.is_ajax and request.method == "POST":

		form = CategoriasForm(request.POST)
		if form.is_valid():
			form.save()
			return JsonResponse({'estado':1})
		else:
			print(form.errors)
			return JsonResponse({'estado':0})