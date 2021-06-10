"""
    AUTHOR:         luis mora
    CREATION DATE:  09/06/2021
    DESCRIPTION:    Modelo de la tabla locatarios del esquema public

    ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

        DATE    ||  MODIFIED_BY ||  DESCRIPTION
    --------------------------------------------------------
                ||              ||  
                ||              ||  
"""

from django.db import models

class Locatario(models.Model):
	"""docstring para modelo local"""
	IdUsuario = models.IntegerField(primary_key=True)
	Nombre = models.CharField(max_length=30)
	Contraceña = models.CharField(max_length=30)
	FechaAlta = models.DateField()
	FechaBaja = models.DateField(blank=True)
	Status = models.IntegerField(help_text="Puede tomar el valor de Activo = 1 o Inactivo = 0")

	class Meta:
		managed = False
		db_table = 'locatario'

	def __str__(self):
		return (self.Nombre,)