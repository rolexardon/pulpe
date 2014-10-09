from django.shortcuts import render_to_response
from django.template import RequestContext

def ver_productos(request):
	return render_to_response('productos.html',context_instance=RequestContext(request))
	
def post_compra(request):
	pass
