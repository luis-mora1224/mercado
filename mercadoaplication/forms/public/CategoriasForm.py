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

Tipo = [
    ('A', 'Articulos para el hogar'),
    ('G', 'Golosinas'),
    ('C', 'Comestibles'),
    ('J', 'Juguetes'),
    ('B', 'Articulos de belleza'),
]
class CategoriasForm(forms.ModelForm):
	"""docstring for CategoriasForm"""
	class Meta:
		model = Categorias

		fields = ('idcategoria','nombre','catedescripcion','catetipo')

		widgets={

				'idcategoria': forms.NumberInput(attrs=   {'id':'cateclave',
                                                         'required':'false',}),
                'nombre': forms.TextInput(attrs=   {'id':'nombre',
                                                        'class':'validate',
                                                        'maxlength':'40',
                                                        'required':'true'}),

				'catedescripcion': forms.TextInput(attrs=   {'id':'catedescripcion',
                                                        'class':'validate',
                                                        'maxlength':'60',
                                                        'required':'true'}),
				'catetipo': forms.TextInput(attrs= {'id':'catetipo',
                                                    'class':'validate',
												    'maxlength':'1',
												    'required':'true'}),
		}
