"""
    AUTHOR:         luis mora
    CREATION DATE:  09/06/2021
    DESCRIPTION:    Modelo de la tabla orden del esquema public

    ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

        DATE    ||  MODIFIED_BY ||  DESCRIPTION
    --------------------------------------------------------
                ||              ||  
                ||              ||  
"""

from django.db import models
from Mercado.mercadoaplication.models.public.producto import Producto

class Orden(models.Model):
	"""docstring for model Orden"""
	IdOrden = models.IntegerField(primary_key=True)
	CantidadProductos = models.IntegerField()
	PrecioTotal = models.FloatField()
	estado = models.IntegerField(help_text="Existen tres números 1=Entregado, 2=pendiente (a recoger o entregar) 3=recolectando")
	servicio = models.CharField(max_length=15, help_text="Domicilio o recoleccion")
	producto = models.ForeignKey(Producto, on_delete=models.CASCADE)

	class Meta:
		managed = False
		db_table = 'orden'

	def __str__(self):
		return (self.estado,)
		