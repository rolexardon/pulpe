<<<<<<< HEAD
from django.shortcuts import render_to_response
from django.template import RequestContext
from inventario.models import producto

def home(request):
	productos = producto.objects.all()
=======
from django.shortcuts import render_to_response
from django.template import RequestContext
from inventario.models import producto

def home(request):
	productos = producto.objects.all()
>>>>>>> fa98660b45de57019fe6f40d7e8f076bce546715
	return render_to_response('home.html',{'productos':productos},context_instance=RequestContext(request))