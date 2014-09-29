from django.contrib import admin
from facturas.models import factura,producto_factura,impuesto,descuento
#from xlutils.copy import copy
#from xlrd import open_workbook, easyxf 

class Producto_FacturaInline(admin.StackedInline):
    model = producto_factura
    extra=0

class FacturasAdmin(admin.ModelAdmin):
	model = factura
	exclude = ("fecha_apertura",'fecha_cierre',)
	inlines = [
		Producto_FacturaInline,
		]
	actions = ['generar_factura']
	def generar_factura(self, request, queryset):
		file_path = ""
		i = datetime.datetime.now()
		ROW = 13
		for factura in queryset:
			rb = open_workbook(file_path,formatting_info=True)
			r_sheet = rb.sheet_by_index(0)

			wb = copy(rb)
			w_sheet = wb.get_sheet(0)
			
			w_sheet.write(5, 4, i.day +"-"+ i.month +"-"+ i.year)
			w_sheet.write(10, 1, factura.cliente.nombre)

			p_fs = producto_factura.objects.filter(factura=factura)
			for item in p_fs:
				w_sheet.write(ROW, 0, item.nombre)
				w_sheet.write(ROW, 1, item.detalles)
				w_sheet.write(ROW, 2, item.cantidad)
				w_sheet.write(ROW, 3, item.producto_precio.precio)
				
			

			wb.save(file_path + '.out' + os.path.splitext(file_path)[-1])
				generar_factura.short_description = "Generar Factura"
		
	def get_readonly_fields(self, request, obj=None):
		if obj: # editing an existing object
			return self.readonly_fields + ('saldo_utilizado',)
		return self.readonly_fields
		
admin.site.register(impuesto)
admin.site.register(descuento)
admin.site.register(factura,FacturasAdmin)


