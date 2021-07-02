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

import json

def vw_categorias(request):
	form = CategoriasForm()
	categorias = Categorias.objects.all().order_by('idcategoria')
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

def vw_categorias_delete(request,pk):

    if request.is_ajax and request.method == "POST":
        try:
        	#pk = request.POST['pk']
        	categoria = Categorias.objects.filter(idcategoria=pk)
        	categoria.delete()
        	return JsonResponse({'valido': 'SI'})
        except:
        	return JsonResponse({'valido': 'No'})


def vw_categorias_Articulos_hogar(request):
	if request.is_ajax and request.method == "POST":
		try:
			valor = request.POST['catetipo']
			categorias = list(Categorias.objects.filter(catetipo = valor).values())#convertimos a un dicionario y a un arreglo
			categoria = json.dumps(categorias)
			#print(categoria)
			return JsonResponse({'valido': categorias})
		except Exception as e:
			print(e)
			return JsonResponse({'valido': 'NO'})
		else:
			return JsonResponse({'valido': 'NO'})

def vw_categorias_actualizar(request, pk):
	if request.is_ajax and request.method == "POST":
		categoriaFiltro = Categorias.objects.get(pk = pk)
		form = CategoriasForm(request.POST, instance = categoriaFiltro)
		if form.is_valid():
			form.save()
			return JsonResponse({'valido':'SI'})
		else:
			return JsonResponse({'valido':'NO'})