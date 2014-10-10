from django.contrib import admin
from facturas.models import factura,producto_factura,impuesto,descuento
from facturas.views import generar_factura

class Producto_FacturaInline(admin.StackedInline):
    model = producto_factura
    extra=0

class FacturasAdmin(admin.ModelAdmin):
	model = factura
	#exclude = ("fecha_apertura",'fecha_cierre',)
	inlines = [
		Producto_FacturaInline,
		]
	list_filter = ('enviada','estado','fecha_apertura','fecha_cierre',)
	search_fields = ['cliente__nombre']
	
	actions = ['enviar_factura']
	def enviar_factura(self, request, queryset):
		for factura in queryset:
			generar_factura(factura)
	enviar_factura.short_description = "Enviar Factura"

	def get_readonly_fields(self, request, obj=None):
		if obj: # editing an existing object
			return self.readonly_fields + ('saldo_utilizado',)
		return self.readonly_fields
		
admin.site.register(impuesto)
admin.site.register(descuento)
admin.site.register(factura,FacturasAdmin)


