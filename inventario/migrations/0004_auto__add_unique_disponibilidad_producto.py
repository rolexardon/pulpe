# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding unique constraint on 'disponibilidad', fields ['producto']
        db.create_unique(u'inventario_disponibilidad', ['producto_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'disponibilidad', fields ['producto']
        db.delete_unique(u'inventario_disponibilidad', ['producto_id'])


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
            'costo': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'detalles': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
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