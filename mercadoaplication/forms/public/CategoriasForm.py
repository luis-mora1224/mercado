"""
    AUTHOR:         luis mora
    CREATION DATE:  28/01/2021
    DESCRIPTION:    Form de la tabla Categorias del esquema public

    ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

        DATE    ||  MODIFIED_BY ||  DESCRIPTION
    --------------------------------------------------------
                ||              ||  
                ||              ||  
"""

from django import forms

#importar modelos
from mercadoaplication.models.Categorias import Categorias

class CategoriasForm(forms.ModelForm):
	"""docstring for CategoriasForm"""
	class Meta:
		model = Categorias

		fields = ('cateclave','catedescripcion','catetipo')

		widgets={

				'cateclave': forms.NumberInput(attrs=   {'id':'cateclave',
                                                         'required':'true',}),

				'catedescripcion': forms.TextInput(attrs=   {'id':'catedescripcion',
                                                        'maxlength':'40',
                                                        'required':'true',
                                                        'oninput':'toUpperCase(this)'}),
				'catetipo': forms.TextInput(attrs= {'id':'catetipo',
												    'maxlength':'1',
												    'required':'true'}),
		}
