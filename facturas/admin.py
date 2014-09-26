from django.contrib import admin
from facturas.models import factura,producto_factura,impuesto,descuento

class Producto_FacturaInline(admin.StackedInline):
    model = producto_factura
    extra=0

class FacturasAdmin(admin.ModelAdmin):
	model = factura
	exclude = ("fecha_apertura",'fecha_cierre',)
	inlines = [
		Producto_FacturaInline,
		]
		
	def get_readonly_fields(self, request, obj=None):
		if obj: # editing an existing object
			return self.readonly_fields + ('saldo_utilizado',)
		return self.readonly_fields
		
admin.site.register(impuesto)
admin.site.register(descuento)
admin.site.register(factura,FacturasAdmin)


