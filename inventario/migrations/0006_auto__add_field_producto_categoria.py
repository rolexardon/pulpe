# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'producto.categoria'
        db.add_column(u'inventario_producto', 'categoria',
                      self.gf('django.db.models.fields.CharField')(default='O', max_length=2),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'producto.categoria'
        db.delete_column(u'inventario_producto', 'categoria')


    models = {
        u'inventario.compra': {
            'Meta': {'object_name': 'compra'},
            'fecha': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'total_compra': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'})
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
            'costo': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'detalles': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'marca': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'precio': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'proveedor': ('django.db.models.fields.CharField', [], {'max_length': '250'})
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
            'costo': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'producto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inventario.producto']"})
        }
    }

    complete_apps = ['inventario']