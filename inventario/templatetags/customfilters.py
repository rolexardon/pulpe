from django import template
from inventario.models import producto,disponibilidad
register = template.Library()

@register.filter(name='get_quantity')
def get_quantity(producto):
	d = disponibilidad.objects.get(producto__pk=producto)
	return str(d.cantidad)
	
@register.filter(name='get_image_url')
def get_image_url(pk):
	p = producto.objects.get(pk=pk)
	if p.imagen:
		return p.imagen.url
	else:
		return "/resources/imgs/productos/none.jpg"

