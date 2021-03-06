from django.shortcuts import render
from django.conf import settings
from facturas.models import producto_factura

from xlutils.copy import copy
from xlrd import open_workbook 
import datetime, os
from django.core.mail import send_mail, EmailMessage, EmailMultiAlternatives


file_path = os.path.join(settings.SITE_ROOT, 'resources/files/')
file_name = 'invoice_template.html'
file_complete_path = file_path + file_name

"""
def generar_factura(factura):
	try:
		i = datetime.datetime.now()
		fecha = str(i.day) + "-" + str(i.month) + "-" + str(i.year)
		ROW = 13
		
		rb = open_workbook(file_complete_path,formatting_info=True)

		wb = copy(rb)
		w_sheet = wb.get_sheet(0)
		
		w_sheet.write(4, 4, fecha)
		w_sheet.write(10, 1, factura.cliente.nombre)

		p_fs = producto_factura.objects.filter(factura=factura)
		for item in p_fs:
			w_sheet.write(ROW, 0, item.producto_precio.producto.nombre)
			w_sheet.write(ROW, 1, item.producto_precio.producto.detalles)
			w_sheet.write(ROW, 2, item.cantidad)
			w_sheet.write(ROW, 3, item.producto_precio.precio)
			
			ROW = ROW +1
			
		save_path = file_path + "facturas_temp/" + str(factura.pk) + "_" + fecha + ".xls" 
		wb.save(save_path)
		
		enviar_correo(save_path,factura.cliente.correo)
		
	except Exception,e:
		print e
"""

def generar_factura(factura):
	try:
		f = open(file_complete_path, 'r')
		linestring  = f.read()
		f.close()
		
		i = datetime.datetime.now()
		fecha = str(i.day) + "-" + str(i.month) + "-" + str(i.year)
		cl = factura.cliente
		
		linestring = linestring.replace('%fecha',fecha)
		linestring = linestring.replace('%num_factura',str(factura.pk))
		linestring = linestring.replace('%cliente',cl.nombre)
		
		p_fs = producto_factura.objects.filter(factura=factura)

		contenido = ''
		for item in p_fs:
			contenido = contenido + ('<tr>' + '<td style= "border-width: 1px; text-align: left; width: 35%; border-radius: 0.25em; border-style: solid; border-color: #989898;">' + item.producto_precio.producto.nombre + '</td>' +
						'<td style= "border-width: 1px; text-align: left; width: 35%; border-radius: 0.25em; border-style: solid; border-color: #989898;">' + item.producto_precio.producto.detalles + '</td>' +
						'<td style= "border-width: 1px; text-align: left; width: 15%; border-radius: 0.25em; border-style: solid; border-color: #989898;">' + str(item.cantidad) + '</td>' +
						'<td style= "border-width: 1px; text-align: left; width: 15%; border-radius: 0.25em; border-style: solid; border-color: #989898;">' + str(item.producto_precio.precio) + '</td>' +
						'<td style= "border-width: 1px; text-align: left; width: 15%; border-radius: 0.25em; border-style: solid; border-color: #989898;">' + str(item.subtotal) + '</td></tr>')
					
		linestring = linestring.replace('%contenido_factura',contenido)
		linestring = linestring.replace('%subtotal',str(factura.subtotal_factura))
		linestring = linestring.replace('%cargos',str(factura.otros_cargos))
		linestring = linestring.replace('%abono',str(factura.total_abonado))
		linestring = linestring.replace('%descuento',str(factura.descuento))
		linestring = linestring.replace('%total',str(factura.total_pendiente))
		linestring = linestring.replace('%saldo',str(factura.saldo_utilizado))
		linestring = linestring.replace('%notas',factura.detalles)
		
		#send_mail('Factura de consumo, fecha: ' + fecha ,'',settings.EMAIL_HOST_USER,[cl.correo], auth_user=None, auth_password=None, connection=None, html_message=linestring)
		
		sent = mailing(cl.correo, 'Factura de consumo, fecha: ' + fecha , linestring)
		if sent:
			factura.enviada = True
			
		factura.save()
	except Exception,e:
		print e
	
def mailing(to,subject,html_content):
	try:
		msg = EmailMultiAlternatives(subject, 'Muchas Gracias' , settings.MY_DEFAULT_EMAIL, [to])
		msg.attach_alternative(html_content, "text/html")
		msg.send()
		return True
	except Exception,e:
		print e
		return False
		
		

			
		
	
	
