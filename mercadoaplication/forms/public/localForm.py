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

		fields = ('nombre', 'pasillo', 'zona')

		widgets = {

				'nombre': forms.TextInput(attrs=   {'id':'nombre',
					                                'maxlength':'30',
					                                'required':'true',
					                                'class':'input-field',
					                                'oninput':'toUpperCase(this)'}),
				'pasillo': forms.NumberInput(attrs=   {'id':'pasillo',
					                                'required':'true',}),
				'zona': forms.TextInput(attrs=   {'id':'zona',
					                                'maxlength':'30',
					                                'class':'input_field'}),
		}