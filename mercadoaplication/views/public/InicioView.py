"""
    AUTHOR:         luis mora
    CREATION DATE:  11/06/2021
    DESCRIPTION:    Vista pagina de inicio

    ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

        DATE    ||  MODIFIED_BY ||  DESCRIPTION
    --------------------------------------------------------
                ||              ||  
                ||              ||  
"""

from django.shortcuts import render, redirect,get_object_or_404
from django.http.response import HttpResponse,JsonResponse,HttpResponseRedirect
from django.contrib import messages

def vw_Inicio(request):
	return render(request, 'public/Inicio.html')