"""
    AUTHOR:         luis mora
    CREATION DATE:  09/06/2021
    DESCRIPTION:    Modelo de la tabla pagos del esquema public

    ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

        DATE    ||  MODIFIED_BY ||  DESCRIPTION
    --------------------------------------------------------
                ||              ||  
                ||              ||  
"""

from django.db import models
from .orden import Orden
from .local import Local


class Pago(models.Model):
	"""docstring for model Pago"""
	IdPago = models.IntegerField(primary_key=True)
	ComisionPorcentaje = models.FloatField()
	ComisionPesos = models.FloatField(help_text="De acuerdo al porcetaje de comision, se agregan los pesos")
	orden = models.ForeignKey(Orden, on_delete=models.CASCADE)
	local = models.ForeignKey(Local, on_delete=models.CASCADE)

	class Meta:
		managed = False
		db_table = 'pago'

	def __str__(self):
		return (self.orden)
		