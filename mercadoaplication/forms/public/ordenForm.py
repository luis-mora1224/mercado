"""
    AUTHOR:         luis mora
    CREATION DATE:  11/06/2021
    DESCRIPTION:    Form de la tabla orden del esquema public

    ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

        DATE    ||  MODIFIED_BY ||  DESCRIPTION
    --------------------------------------------------------
                ||              ||  
                ||              ||  
"""
#importar modelos
from mercadoaplication.models.orden import Orden

from django import forms

class OrdenForm(models.Model):
	"""docstring for ordenForm"""
	model = Orden

	fields =  ('cantidadproductos', 'preciototal', 'estado',
		       'servicio', 'producto')
	widgets = {
			'cantidadproductos': forms.NumberInput(attrs=   {'id':'cantidadproductos',
				                                            'required':'true'}),
			'preciototal': forms.FloatField(attrs= {'id':'preciototal',
				                                    'step': '0.01'}),
			'estado': forms.NumberInput(attrs=   {'id':'estado',
				                                    'required':'true'}),
			'servicio': forms.TextInput(attrs = {'id':'estado',
				                                    'maxlength':'30',
					                                'required':'true',
					                                'class':'input-field',}),
	}