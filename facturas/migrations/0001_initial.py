# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'factura'
        db.create_table(u'facturas_factura', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cliente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['clientes.cliente'])),
            ('estado', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('fecha_apertura', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('fecha_cierra', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'facturas', ['factura'])

        # Adding model 'producto_factura'
        db.create_table(u'facturas_producto_factura', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('factura', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['facturas.factura'])),
            ('producto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inventario.producto'])),
            ('precio_actual', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2)),
            ('cantidad', self.gf('django.db.models.fields.IntegerField')()),
            ('subtotal', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2)),
        ))
        db.send_create_signal(u'facturas', ['producto_factura'])


    def backwards(self, orm):
        # Deleting model 'factura'
        db.delete_table(u'facturas_factura')

        # Deleting model 'producto_factura'
        db.delete_table(u'facturas_producto_factura')


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
            'fecha_cierra': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'facturas.producto_factura': {
            'Meta': {'object_name': 'producto_factura'},
            'cantidad': ('django.db.models.fields.IntegerField', [], {}),
            'factura': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['facturas.factura']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'precio_actual': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'producto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inventario.producto']"}),
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
        }
    }

    complete_apps = ['facturas']