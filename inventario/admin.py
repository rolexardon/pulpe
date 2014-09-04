from django.contrib import admin
from inventario.models import producto,disponibilidad,compra,producto_compra,producto_abastecimiento


class Producto_CompraInline(admin.StackedInline):
    model = producto_compra
    extra=0

class ComprasAdmin(admin.ModelAdmin):
	model = compra
	inlines = [
		Producto_CompraInline,
		]
	
		   
admin.site.register(producto)
admin.site.register(disponibilidad)
admin.site.register(compra,ComprasAdmin)
#admin.site.register(producto_compra)
admin.site.register(producto_abastecimiento)

