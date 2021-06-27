"""
    AUTHOR:         luis mora
    CREATION DATE:  21/06/2021
    DESCRIPTION:    Form de la tabla promocion del esquema public

    ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

        DATE    ||  MODIFIED_BY ||  DESCRIPTION
    --------------------------------------------------------
                ||              ||  
                ||              ||  
"""
#importar modelos
from mercadoaplication.models.promocion import Promocion

from django import forms

class PromocionForm(forms.ModelForm):
	class Meta:
		models = Promocion

		fields = ('nombre', 'numeroproductos', 'preciopromocion')

		widgets = {
				'nombre': forms.TextInput(attrs=   {'id':'nombre',
				  	                                'maxlength':'30',
					                                'required':'true',
					                                'class':'input-field',
					                                'oninput':'toUpperCase(this)'}),
				'numeroproductos': forms.NumberInput(attrs=   {'id':'comisionporcentaje'}),
				'preciopromocion': forms.FloatField(attrs=   {'id':'existencia',
														  'step': '0.01'})

		}