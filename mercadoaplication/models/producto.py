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

from .Categorias import Categorias
from .local import Local1

from django.db import models


class Producto(models.Model):
    idproducto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40)
    precioventa = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    existencia = models.IntegerField(blank=True, null=True)
    idcategoria = models.ForeignKey(Categorias, models.DO_NOTHING, db_column='idcategoria', blank=True, null=True)
    idlocal = models.ForeignKey(Local1, models.DO_NOTHING, db_column='idlocal', blank=True, null=True)
    idpromocion = models.ForeignKey('Promocion', models.DO_NOTHING, db_column='idpromocion', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'producto'

    def __str__(self):
    	return (self.nombre, self.existencia,)