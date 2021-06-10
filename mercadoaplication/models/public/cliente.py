"""
    AUTHOR:         luis mora
    CREATION DATE:  09/06/2021
    DESCRIPTION:    Modelo de la tabla cliente del esquema public

    ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

        DATE    ||  MODIFIED_BY ||  DESCRIPTION
    --------------------------------------------------------
                ||              ||  
                ||              ||  
"""

from django.db import models
from .orden import Orden


class Cliente(models.Model):
	"""docstring for model Cliente"""
	IdCliente = models.IntegerField(primary_key=True)
	Nombre = models.CharField(max_length=30)
	Contraceña = models.CharField(max_length=30)
	Direccion = models.CharField(max_length=50, blank=True)
	Status = models.IntegerField(help_text="Puede tomar el valor de Activo = 1 o Inactivo = 0")
	orden = models.ForeignKey(Orden, on_delete=models.CASCADE)

	class Meta:
		managed = False
		db_table = 'cliente'

	def __str__(self):
		return (self.Nombre)