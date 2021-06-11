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

		fields = ('Nombre', 'Contraceña', 'Direccion',
			      'FechaAlta', 'FechaBaja', 'Status')

		widgets = {
				  'Nombre': forms.TextInput(attrs=   {'id':'Nombre',
				  									  'maxlength':'30',
				  									  'required':'true',
				  									  'class': 'input-field',
				  									  'oninput':'toUpperCase'}),
				  'Contraceña': forms.TextInput(attrs=   {'id':'Contraceña',
				  	                                  'maxlength':'30',
				  	                                  'required':'true',
				  	                                  'class':'input-field'}),
				  'Direccion': forms.TextInput(attrs=   {'id':'Direccion',
				  	                                  'maxlength':'30',
				  									  'required':'true',
				  									  'class': 'input-field',}),
				  'FechaAlta': forms.DateField(attrs= {'id':'FechaAlta'}),

				  'FechaAlta': forms.DateField(attrs=   {'id':'FechaBaja',}),

				  'Status': forms.TextInput(attrs=   {'id':'Status', 
				  	                                  'maxlength':'12',
				  	                                  'required':'true',
				  	                                  'class':'input-field'}),
		}