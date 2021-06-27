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
    idusuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40)
    contraceña = models.CharField(max_length=40)
    fechaalta = models.DateField(blank=True, null=True)
    fechabaja = models.DateField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'locatario'

    def __str__(self):
    	return (self.nombre,)