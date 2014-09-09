from django.shortcuts import render_to_response
from django.template import RequestContext
from inventario.models import producto

def home(request):
	productos = producto.objects.all()
	return render_to_response('home.html',{'productos':productos},context_instance=RequestContext(request))