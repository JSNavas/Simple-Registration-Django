from django import forms
from .models import Registrado

class RegistradoForm(forms.ModelForm):
	class Meta:
		model = Registrado
		fields = ['user','email', 'media']

	# metodos para hacer validaciones por cada campo solo colocando clean_nombreDelCampo(self):
	def clean_user(self):
		user = self.cleaned_data['user'] # cleaned_data devuelve un dicionario con los elementos validos
		
		# validar que no se ingresen solo numero en el campo usuario
		if user.isdigit():
			raise forms.ValidationError("El nombre de usuario no puede contener solo numeros")

		return user

	def clean_email(self):
		email = self.cleaned_data['email']

		# valida que se ingrese un determino correo electronico
		# if not email.endswith("@gmail.com"):
		# 	raise forms.ValidationError("Utilice un correo gmail.com")

		return email