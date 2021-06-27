"""
    AUTHOR:         luis mora
    CREATION DATE:  11/06/2021
    DESCRIPTION:    Form de la tabla locatario del esquema public

    ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

        DATE    ||  MODIFIED_BY ||  DESCRIPTION
    --------------------------------------------------------
                ||              ||  
                ||              ||  
"""
#importar modelos
from mercadoaplication.models.locatario import Locatario

from django import forms

class locatarioForm(forms.ModelForm):
	"""docstring for locatarioForm"""
	class Meta:
		model = Locatario

		fields = ('nombre', 'contraceña','fechaalta', 
			      'fechabaja', 'status')

		widgets = {
				  'nombre': forms.TextInput(attrs=   {'id':'nombre',
				  									  'maxlength':'30',
				  									  'required':'true',
				  									  'class': 'input-field',
				  									  'oninput':'toUpperCase(this)'}),
				  'contraceña': forms.TextInput(attrs=   {'id':'contraceña',
				  	                                  'maxlength':'30',
				  	                                  'required':'true',
				  	                                  'class':'input-field'}),
		
				  'fechaalta': forms.DateField(attrs= {'id':'fechaalta'}),

				  'fechaalta': forms.DateField(attrs=   {'id':'fechabaja',}),

				  'status': forms.TextInput(attrs=   {'id':'status', 
				  	                                  'maxlength':'12',
				  	                                  'required':'true',
				  	                                  'class':'input-field'}),
		}
