"""
    AUTHOR:         luis mora
    CREATION DATE:  21/06/2021
    DESCRIPTION:    Modelo de la tabla promocion del esquema public

    ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

        DATE    ||  MODIFIED_BY ||  DESCRIPTION
    --------------------------------------------------------
                ||              ||  
                ||              ||  
"""

from django.db import models

class Promocion(models.Model):
    idpromocion = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40)
    numeroproductos = models.IntegerField(blank=True, null=True)
    preciopromocion = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'promocion'

    def __str__(self):
    	return (self.nombre,)