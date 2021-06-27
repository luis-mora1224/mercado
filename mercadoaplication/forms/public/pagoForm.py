"""
    AUTHOR:         luis mora
    CREATION DATE:  11/06/2021
    DESCRIPTION:    Form de la tabla pago del esquema public

    ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

        DATE    ||  MODIFIED_BY ||  DESCRIPTION
    --------------------------------------------------------
                ||              ||  
                ||              ||  
"""
#importar modelos
from mercadoaplication.models.pago import Pago

from django import forms

class PagoForm(forms.ModelForm):
	class Meta:
		model = Pago

		fields = ('comisionporcentaje', 'comisionpesos')

		widgets = {

				   'ComisionPorcentaje': forms.FloatField(attrs=   {'id':'ComisionPorcentaje',
				   	                                                'step': '0.01'}),
				   'ComisionPesos': forms.FloatField(attrs=   {'id':'ComisionPorcentaje',
				   	                                                'step': '0.01'})
		}
