"""
    AUTHOR:         luis mora
    CREATION DATE:  09/06/2021
    DESCRIPTION:    Modelo de la tabla producto del esquema public

    ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

        DATE    ||  MODIFIED_BY ||  DESCRIPTION
    --------------------------------------------------------
                ||              ||  
                ||              ||  
"""

from Mercado.mercadoaplication.models.public.categorias import Categorias
from Mercado.mercadoaplication.models.public.local import Local

from django.db import models


class Producto(models.Model):
	IdProducto = models.IntegerField(primary_key=True)
	Nombre = models.CharField(max_length=40)
	PrecioVenta = models.FloatField()
	Existencia = models.IntegerField()
	categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)
	local = models.ForeignKey(Local, on_delete=models.CASCADE)

	class Meta:
		managed = False
		db_table = 'producto'

	def __str__(self):
		return (self.Nombre, self.Existencia,)