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

	fields =  ('CantidadProductos', 'PrecioTotal', 'estado',
		       'servicio', 'producto')
	widgets = {
			'CantidadProductos': forms.NumberInput(attrs=   {'id':'CantidadProductos',
				                                            'required':'true'}),
			'PrecioTotal': forms.FloatField(attrs= {'id':'PrecioTotal',
				                                    'step': '0.01'}),
			'estado': forms.NumberInput(attrs=   {'id':'estado',
				                                    'required':'true'}),
			'servicio': forms.TextInput(attrs = {'id':'estado',
				                                    'maxlength':'30',
					                                'required':'true',
					                                'class':'input-field',}),
			'producto': forms.NumberInput(attrs=   {'id':'producto',
				                                    'required':'true'})
	}