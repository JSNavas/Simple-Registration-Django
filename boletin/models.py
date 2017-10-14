from __future__ import unicode_literals

from django.db import models

# Create your models here.

# ejecutar makemigrations y migrate para guardar el nuevo modelo y cada cambio que se realice en dicho modelo
class Registrado(models.Model):
	user = models.CharField(max_length=50)
	email = models.EmailField()
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	actualizado = models.DateTimeField(auto_now_add=False, auto_now=True)
	media = models.FileField(upload_to="myfolder/", blank=True, null=True)

	# campo que se va a mostrar de primero en la vista admin
	def __unicode__(self): # python3 __str___
		return self.email 