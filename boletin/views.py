from django.shortcuts import render
from .forms import RegistradoForm
from .models import Registrado

# Create your views here.
def home(request):
	form = RegistradoForm(request.POST or None, request.FILES or None) # (request.POST) para validar la informacion mandada por post mostrando los errores con el (or None) evita mostrarlo si no es necesario
	
	# QuerySet para almacenar todos los elementos del modelo para hacer bucles
	queryset = Registrado.objects.all()

	# for obj in queryset:
	# 	print obj
	# 	print obj.id
	# 	print obj.user
	# 	print obj.email


	titulo = "Formulario de Registro"

	# valida si el usuario esta logeado
	# if request.user.is_authenticated():
	# 	titulo = "Bienvenido, %s" % (request.user)

	# diccionario donde se manda los datos al template
	context = {
		"titulo": titulo,
		"form": form,
		"registrados": queryset
	}

	# instance = form.save(commit=False) para no guardar en la base de datos
	# print instance.email

	# se valida si la informacion mandada en el formulario es valida
	if form.is_valid():
		form.save()

		usuario = form.cleaned_data['user']
		context = {
			"titulo": "Gracias %s, ya te hemos registrado!" % (usuario) 
		}

	return render(request, "home.html", context)

def about(request):
	titulo = "Sobre nosotros"

	context = {
		"titulo": titulo,
	}

	return render(request, "about.html", context)