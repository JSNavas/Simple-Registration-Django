from django.contrib import admin

from .models import Registrado # se importa de models.py el modelo Registrado
from .forms import RegistradoForm # se importa de forms.py el modelo RegistradoForm

# Register your models here.
class AdminRegistrado(admin.ModelAdmin):
	list_display = ['__unicode__','user','timestamp', 'actualizado']
	# list_display_links = ['user'] se indica que elemento va a tener el enlace en la vista admin
	list_filter = ['timestamp']
	list_editable = ['user']
	search_fields = ['email', 'user']
	form = RegistradoForm

admin.site.register(Registrado, AdminRegistrado) # registramos los modelos en el panel de admin