from django.shortcuts import render
from facturas.models import producto_factura
#from xlutils.copy import copy
#from xlrd import open_workbook, easyxf 
import datetime
from win32com import client
file_path = ""

def generar_factura(factura):
	try:
		i = datetime.datetime.now()
		fecha = i.day +"-"+ i.month +"-"+ i.year
		ROW = 13
		
		rb = open_workbook(file_path,formatting_info=True)
		r_sheet = rb.sheet_by_index(0)

		wb = copy(rb)
		w_sheet = wb.get_sheet(0)
		
		w_sheet.write(5, 4, fecha)
		w_sheet.write(10, 1, factura.cliente.nombre)

		p_fs = producto_factura.objects.filter(factura=factura)
		for item in p_fs:
			w_sheet.write(ROW, 0, item.nombre)
			w_sheet.write(ROW, 1, item.detalles)
			w_sheet.write(ROW, 2, item.cantidad)
			w_sheet.write(ROW, 3, item.producto_precio.precio)
			
			ROW = ROW +1
			
		save_path = file_path + fecha
		wb.save(save_path)
		
		xlApp = win32com.client.Dispatch("Excel.Application")
		books = xlApp.Workbooks.Open(save_path)
		ws = books.Worksheets[0]
		ws.Visible = 1
		ws.ExportAsFixedFormat(0, 'C:\\excel\\trial.pdf')
		
		enviar_correo(save_path,factura.cliente.correo)
		
	except Exception,e:
		print e
	
def enviar_correo(path,mail):
	try:
		pass
	except Exception,e:
		print e
	