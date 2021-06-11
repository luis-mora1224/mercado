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

		fields = ('Nombre', 'Contraceña','FechaAlta', 
			      'FechaBaja', 'Status')

		widgets = {
				  'Nombre': forms.TextInput(attrs=   {'id':'Nombre',
				  									  'maxlength':'30',
				  									  'required':'true',
				  									  'class': 'input-field',
				  									  'oninput':'toUpperCase(this)'}),
				  'Contraceña': forms.TextInput(attrs=   {'id':'Contraceña',
				  	                                  'maxlength':'30',
				  	                                  'required':'true',
				  	                                  'class':'input-field'}),
		
				  'FechaAlta': forms.DateField(attrs= {'id':'FechaAlta'}),

				  'FechaAlta': forms.DateField(attrs=   {'id':'FechaBaja',}),

				  'Status': forms.TextInput(attrs=   {'id':'Status', 
				  	                                  'maxlength':'12',
				  	                                  'required':'true',
				  	                                  'class':'input-field'}),
		}
