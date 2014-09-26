from django.contrib import admin
from inventario.models import producto,proveedor,producto_costo,producto_precio,disponibilidad,compra,producto_compra,producto_abastecimiento

class Producto_CompraInline(admin.StackedInline):
    model = producto_compra
    extra=0

class ComprasAdmin(admin.ModelAdmin):
	model = compra
	#exclude = ("total_compra",)
	inlines = [
		Producto_CompraInline,
		]
	"""	
	def get_readonly_fields(self, request, obj=None):
		if obj: # editing an existing object
			return self.readonly_fields + ('total_compra',)
		return self.readonly_fields
	"""
		
class PCosto_Admin(admin.ModelAdmin):
	model = producto_costo
	list_filter = ('activo',)
	
	search_fields = ['producto__nombre']

class PPrecio_Admin(admin.ModelAdmin):
	model = producto_precio
	list_filter = ('activo',)
	
	search_fields = ['producto__nombre']

		   
admin.site.register(producto)
admin.site.register(disponibilidad)
admin.site.register(compra,ComprasAdmin)
#admin.site.register(producto_compra)
admin.site.register(producto_abastecimiento)
admin.site.register(proveedor)
admin.site.register(producto_costo,PCosto_Admin)
admin.site.register(producto_precio,PPrecio_Admin)

