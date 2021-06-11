"""
    AUTHOR:         luis mora
    CREATION DATE:  11/06/2021
    DESCRIPTION:    Form de la tabla producto del esquema public

    ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

        DATE    ||  MODIFIED_BY ||  DESCRIPTION
    --------------------------------------------------------
                ||              ||  
                ||              ||  
"""
#importar modelos
from mercadoaplication.models.producto import Producto

from django import forms

class ProductoForm(forms.ModelForm):
	class Meta:
		model = Producto

		fields = ('Nombre', 'PrecioVenta', 'Existencia',
			      'categoria', 'local')
		widgets = {

				  'Nombre': forms.TextInput(attrs=   {'id':'Nombre',
				  	                                'maxlength':'30',
					                                'required':'true',
					                                'class':'input-field',
					                                'oninput':'toUpperCase(this)'}),
				  'PrecioVenta': forms.FloatField(attrs=   {'id':'ComisionPorcentaje',
				   	                                                'step': '0.01'}),
				  'Existencia': forms.NumberInput(attrs=   {'id':'orden',}),
				  'categoria': forms.NumberInput(attrs=   {'id':'orden',}),
				  'local': forms.NumberInput(attrs=   {'id':'orden',}),
		}
