from django import template
from inventario.models import producto,disponibilidad
import os

register = template.Library()


@register.filter(name='get_quantity')
def get_quantity(producto):
	d = disponibilidad.objects.filter(producto__pk=producto)
	if d:
		return str(d[0].cantidad)
	else:
		return 0
	
@register.filter(name='get_image_url')
def get_image_url(pk):
	p = producto.objects.get(pk=pk)
	if p.imagen:
		return os.path.basename(p.imagen.url)
	else:
		return "none.jpg"

