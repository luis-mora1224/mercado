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
from .producto import Producto
from .local import Local1
from .cliente import Cliente

class Orden(models.Model):
    idorden = models.AutoField(primary_key=True)
    cantidadproductos = models.IntegerField(blank=True, null=True)
    preciototal = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    estado = models.IntegerField(blank=True, null=True)
    servicio = models.CharField(max_length=35)
    idproducto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='idproducto', blank=True, null=True)
    idlocal = models.ForeignKey(Local1, models.DO_NOTHING, db_column='idlocal', blank=True, null=True)
    idcliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='idcliente', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orden'

    def __str__(self):
    	return (self.servicio)
		