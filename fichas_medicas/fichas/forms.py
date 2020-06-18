from django import forms
from .models import Ficha

class FichaForm(forms.ModelForm):

	class Meta:
		model = Ficha
		fields = ("paciente","descripcion",)
		labels = {
			'descripcion': 'Contenido',
			'paciente': 'Paciente'
		}

