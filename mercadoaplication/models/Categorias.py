"""
    AUTHOR:         luis mora
    CREATION DATE:  01/05/2021
    DESCRIPTION:    Modelo de la tabla Categorias del esquema public

    ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

        DATE    ||  MODIFIED_BY ||  DESCRIPTION
    --------------------------------------------------------
                ||              ||  
                ||              ||  
"""

from django.db import models

class Categorias(models.Model):
    cateclave = models.IntegerField(primary_key=True)
    catedescripcion = models.CharField(max_length=40)
    catetipo = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categorias'

    #este atributo nos da una referencia para saber que objeto se invoca al hacer una instancia
    def __str__(self):
        return (self.catedescripcion,)