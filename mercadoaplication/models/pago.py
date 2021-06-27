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
from .local import Local1


class Pago(models.Model):
    idpagos = models.AutoField(primary_key=True)
    comisionporcentaje = models.DecimalField(max_digits=2, decimal_places=2, blank=True, null=True)
    comisionpesos = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    idorden = models.ForeignKey(Orden, models.DO_NOTHING, db_column='idorden', blank=True, null=True)
    idlocal = models.ForeignKey(Local1, models.DO_NOTHING, db_column='idlocal', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pago'

    def __str__(self):
    	return (self.orden,)		