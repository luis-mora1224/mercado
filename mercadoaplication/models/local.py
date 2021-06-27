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
from .locatario import Locatario

class Local1(models.Model):
    idlocal = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40)
    pasillo = models.IntegerField(blank=True, null=True)
    zona = models.CharField(max_length=30, blank=True, null=True)
    idusuario = models.ForeignKey('Locatario', models.DO_NOTHING, db_column='idusuario', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'local1'

    def __str__(self):
    	return(self.nombre,)
    	