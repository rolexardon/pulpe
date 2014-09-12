# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'producto'
        db.create_table(u'inventario_producto', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('marca', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('imagen', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('detalles', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('categoria', self.gf('django.db.models.fields.CharField')(max_length=2)),
        ))
        db.send_create_signal(u'inventario', ['producto'])

        # Adding model 'proveedor'
        db.create_table(u'inventario_proveedor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('direccion', self.gf('django.db.models.fields.CharField')(max_length=500)),
        ))
        db.send_create_signal(u'inventario', ['proveedor'])

        # Adding model 'producto_costo'
        db.create_table(u'inventario_producto_costo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('producto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inventario.producto'])),
            ('proveedor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inventario.proveedor'])),
            ('costo', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2)),
            ('activo', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('fecha_ingreso', self.gf('django.db.models.fields.DateField')()),
            ('fecha_debaja', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'inventario', ['producto_costo'])

        # Adding unique constraint on 'producto_costo', fields ['producto', 'proveedor', 'costo']
        db.create_unique(u'inventario_producto_costo', ['producto_id', 'proveedor_id', 'costo'])

        # Adding model 'producto_precio'
        db.create_table(u'inventario_producto_precio', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('producto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inventario.producto'])),
            ('precio', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2)),
            ('activo', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('fecha_ingreso', self.gf('django.db.models.fields.DateField')()),
            ('fecha_debaja', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'inventario', ['producto_precio'])

        # Adding unique constraint on 'producto_precio', fields ['producto', 'precio']
        db.create_unique(u'inventario_producto_precio', ['producto_id', 'precio'])

        # Adding model 'disponibilidad'
        db.create_table(u'inventario_disponibilidad', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('producto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inventario.producto'], unique=True)),
            ('cantidad', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'inventario', ['disponibilidad'])

        # Adding model 'compra'
        db.create_table(u'inventario_compra', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fecha', self.gf('django.db.models.fields.DateField')()),
            ('total_compra', self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=6, decimal_places=2)),
        ))
        db.send_create_signal(u'inventario', ['compra'])

        # Adding model 'producto_compra'
        db.create_table(u'inventario_producto_compra', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('compra', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inventario.compra'])),
            ('producto_costo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inventario.producto_costo'])),
            ('cantidad', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'inventario', ['producto_compra'])

        # Adding model 'producto_abastecimiento'
        db.create_table(u'inventario_producto_abastecimiento', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('producto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inventario.producto'])),
            ('minimo', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'inventario', ['producto_abastecimiento'])


    def backwards(self, orm):
        # Removing unique constraint on 'producto_precio', fields ['producto', 'precio']
        db.delete_unique(u'inventario_producto_precio', ['producto_id', 'precio'])

        # Removing unique constraint on 'producto_costo', fields ['producto', 'proveedor', 'costo']
        db.delete_unique(u'inventario_producto_costo', ['producto_id', 'proveedor_id', 'costo'])

        # Deleting model 'producto'
        db.delete_table(u'inventario_producto')

        # Deleting model 'proveedor'
        db.delete_table(u'inventario_proveedor')

        # Deleting model 'producto_costo'
        db.delete_table(u'inventario_producto_costo')

        # Deleting model 'producto_precio'
        db.delete_table(u'inventario_producto_precio')

        # Deleting model 'disponibilidad'
        db.delete_table(u'inventario_disponibilidad')

        # Deleting model 'compra'
        db.delete_table(u'inventario_compra')

        # Deleting model 'producto_compra'
        db.delete_table(u'inventario_producto_compra')

        # Deleting model 'producto_abastecimiento'
        db.delete_table(u'inventario_producto_abastecimiento')


    models = {
        u'inventario.compra': {
            'Meta': {'object_name': 'compra'},
            'fecha': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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