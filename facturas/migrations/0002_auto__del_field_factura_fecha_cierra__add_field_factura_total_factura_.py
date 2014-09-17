# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'factura.fecha_cierra'
        db.delete_column(u'facturas_factura', 'fecha_cierra')

        # Adding field 'factura.total_factura'
        db.add_column(u'facturas_factura', 'total_factura',
                      self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=6, decimal_places=2),
                      keep_default=False)

        # Adding field 'factura.total_abonado'
        db.add_column(u'facturas_factura', 'total_abonado',
                      self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=6, decimal_places=2),
                      keep_default=False)

        # Adding field 'factura.total_pendiente'
        db.add_column(u'facturas_factura', 'total_pendiente',
                      self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=6, decimal_places=2),
                      keep_default=False)

        # Adding field 'factura.fecha_cierre'
        db.add_column(u'facturas_factura', 'fecha_cierre',
                      self.gf('django.db.models.fields.DateField')(null=True, blank=True),
                      keep_default=False)

        # Deleting field 'producto_factura.precio_actual'
        db.delete_column(u'facturas_producto_factura', 'precio_actual')

        # Deleting field 'producto_factura.producto'
        db.delete_column(u'facturas_producto_factura', 'producto_id')

        # Adding field 'producto_factura.producto_precio'
        db.add_column(u'facturas_producto_factura', 'producto_precio',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0.0, to=orm['inventario.producto_precio']),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'factura.fecha_cierra'
        db.add_column(u'facturas_factura', 'fecha_cierra',
                      self.gf('django.db.models.fields.DateField')(null=True, blank=True),
                      keep_default=False)

        # Deleting field 'factura.total_factura'
        db.delete_column(u'facturas_factura', 'total_factura')

        # Deleting field 'factura.total_abonado'
        db.delete_column(u'facturas_factura', 'total_abonado')

        # Deleting field 'factura.total_pendiente'
        db.delete_column(u'facturas_factura', 'total_pendiente')

        # Deleting field 'factura.fecha_cierre'
        db.delete_column(u'facturas_factura', 'fecha_cierre')

        # Adding field 'producto_factura.precio_actual'
        db.add_column(u'facturas_producto_factura', 'precio_actual',
                      self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=6, decimal_places=2),
                      keep_default=False)

        # Adding field 'producto_factura.producto'
        db.add_column(u'facturas_producto_factura', 'producto',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0.0, to=orm['inventario.producto']),
                      keep_default=False)

        # Deleting field 'producto_factura.producto_precio'
        db.delete_column(u'facturas_producto_factura', 'producto_precio_id')


    models = {
        u'clientes.cliente': {
            'Meta': {'object_name': 'cliente'},
            'apellido': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'cargo': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'celular': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'correo': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '70'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'facturas.factura': {
            'Meta': {'object_name': 'factura'},
            'cliente': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['clientes.cliente']"}),
            'estado': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'fecha_apertura': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'fecha_cierre': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'total_abonado': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '6', 'decimal_places': '2'}),
            'total_factura': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '6', 'decimal_places': '2'}),
            'total_pendiente': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '6', 'decimal_places': '2'})
        },
        u'facturas.producto_factura': {
            'Meta': {'object_name': 'producto_factura'},
            'cantidad': ('django.db.models.fields.IntegerField', [], {}),
            'factura': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['facturas.factura']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'producto_precio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inventario.producto_precio']"}),
            'subtotal': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'})
        },
        u'inventario.producto': {
            'Meta': {'object_name': 'producto'},
            'categoria': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'detalles': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'marca': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'inventario.producto_precio': {
            'Meta': {'unique_together': "(('producto', 'precio'),)", 'object_name': 'producto_precio'},
            'activo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'fecha_debaja': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'fecha_ingreso': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'precio': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'producto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inventario.producto']"})
        }
    }

    complete_apps = ['facturas']