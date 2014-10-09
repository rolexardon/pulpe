# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'compra.detalles'
        db.add_column(u'inventario_compra', 'detalles',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'compra.imagen'
        db.add_column(u'inventario_compra', 'imagen',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'compra.detalles'
        db.delete_column(u'inventario_compra', 'detalles')

        # Deleting field 'compra.imagen'
        db.delete_column(u'inventario_compra', 'imagen')


    models = {
        u'inventario.compra': {
            'Meta': {'object_name': 'compra'},
            'detalles': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'total_compra': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '6', 'decimal_places': '2'})
        },
        u'inventario.disponibilidad': {
            'Meta': {'object_name': 'disponibilidad'},
            'cantidad': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'producto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inventario.producto']", 'unique': 'True'})
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
        u'inventario.producto_abastecimiento': {
            'Meta': {'object_name': 'producto_abastecimiento'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'minimo': ('django.db.models.fields.IntegerField', [], {}),
            'producto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inventario.producto']"})
        },
        u'inventario.producto_compra': {
            'Meta': {'object_name': 'producto_compra'},
            'cantidad': ('django.db.models.fields.IntegerField', [], {}),
            'compra': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inventario.compra']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'producto_costo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inventario.producto_costo']"})
        },
        u'inventario.producto_costo': {
            'Meta': {'unique_together': "(('producto', 'proveedor', 'costo'),)", 'object_name': 'producto_costo'},
            'activo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'costo': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'fecha_debaja': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'fecha_ingreso': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'producto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inventario.producto']"}),
            'proveedor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inventario.proveedor']"})
        },
        u'inventario.producto_precio': {
            'Meta': {'unique_together': "(('producto', 'precio'),)", 'object_name': 'producto_precio'},
            'activo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'fecha_debaja': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'fecha_ingreso': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'precio': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'producto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inventario.producto']"})
        },
        u'inventario.proveedor': {
            'Meta': {'object_name': 'proveedor'},
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        }
    }

    complete_apps = ['inventario']