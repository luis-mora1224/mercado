"""
    AUTHOR:         luis mora
    CREATION DATE:  11/06/2021
    DESCRIPTION:    Form de la tabla cliente del esquema public

    ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

        DATE    ||  MODIFIED_BY ||  DESCRIPTION
    --------------------------------------------------------
                ||              ||  
                ||              ||  
"""
#importar modelos
from mercadoaplication.models.cliente import Cliente

from django import forms

class ClienteForm(forms.ModelForm):
	class Meta:
		model = Cliente

		fields = ('nombre', 'contraceña', 'direccion',
			      'status')

		widgets = {
				  'nombre': forms.TextInput(attrs=   {'id':'nombre',
				  									  'maxlength':'30',
				  									  'required':'true',
				  									  'class': 'input-field'}),
				  'contraceña': forms.TextInput(attrs=   {'id':'contraceña',
				  	                                  'maxlength':'30',
				  	                                  'required':'true',
				  	                                  'class':'input-field'}),
				  'direccion': forms.TextInput(attrs=   {'id':'direccion',
				  	                                  'maxlength':'30',
				  									  'required':'true',
				  									  'class': 'input-field',}),
				  'Status': forms.TextInput(attrs=   {'id':'Status', 
				  	                                  'maxlength':'12',
				  	                                  'required':'true',
				  	                                  'class':'input-field'}),
		}