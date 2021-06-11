"""
    AUTHOR:         luis mora
    CREATION DATE:  11/06/2021
    DESCRIPTION:    Form de la tabla local del esquema public

    ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

        DATE    ||  MODIFIED_BY ||  DESCRIPTION
    --------------------------------------------------------
                ||              ||  
                ||              ||  
"""
#importar modelos
from mercadoaplication.models.local import Local

from django import forms

class LocalForm(forms.ModelForm):
	"""docstring for LocalForm"""
	class Meta:
		model = Local

		fields = ('Nombre', 'Pasillo', 'Zona',
			      'locatarios')

		widgets = {

				'Nombre': forms.TextInput(attrs=   {'id':'Nombre',
					                                'maxlength':'30',
					                                'required':'true',
					                                'class':'input-field',
					                                'oninput':'toUpperCase(this)'}),
				'Pasillo': forms.NumberInput(attrs=   {'id':'Pasillo',
					                                'required':'true',}),
				'Zona': forms.TextInput(attrs=   {'id':'Zona',
					                                'maxlength':'30',
					                                'class':'input_field'}),
				'locatarios': forms.NumberInput(attrs=   {'id':'locatarios',
					                                'class':'input_field'}),
		}