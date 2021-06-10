"""
    AUTHOR:         luis mora
    CREATION DATE:  09/06/2021
    DESCRIPTION:    Modelo de la tabla local del esquema public

    ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

        DATE    ||  MODIFIED_BY ||  DESCRIPTION
    --------------------------------------------------------
                ||              ||  
                ||              ||  
"""

from django.db import models
from Mercado.mercadoaplication.models.public.locatario import Locatario

class Local(models.Model):
	"""docstring para modelo local"""
	Idlocal = models.IntegerField(primary_key=True)
	Nombre = models.CharField(max_length=30)
	Pasillo = models.IntegerField()
	Zona = models.CharField(max_length=30, blank=True)
	locatarios = models.ForeignKey(Locatario, on_delete=models.CASCADE)

	class Meta:
		managed = False
		db_table = 'local'

	def __str__(self):
		return (self.Nombre,)