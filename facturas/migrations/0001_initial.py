
# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'impuesto'
        db.create_table(u'facturas_impuesto', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('identificador', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('valor_decimal', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2)),
        ))
        db.send_create_signal(u'facturas', ['impuesto'])

        # Adding model 'descuento'
        db.create_table(u'facturas_descuento', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('identificador', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('valor_decimal', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2)),
        ))
        db.send_create_signal(u'facturas', ['descuento'])

        # Adding model 'factura'
        db.create_table(u'facturas_factura', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cliente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['clientes.cliente'])),
            ('estado', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('metodo_pago', self.gf('django.db.models.fields.IntegerField')(default=6)),
            ('detalles', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('enviada', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('impuesto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['facturas.impuesto'], null=True, blank=True)),
            ('descuento', self.gf('django.db.models.fields.DecimalField')(default=0.0, null=True, max_digits=6, decimal_places=2)),
            ('saldo_utilizado', self.gf('django.db.models.fields.DecimalField')(default=0.0, null=True, max_digits=6, decimal_places=2)),
            ('subtotal_factura', self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=6, decimal_places=2)),
            ('total_factura', self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=6, decimal_places=2)),
            ('total_abonado', self.gf('django.db.models.fields.DecimalField')(default=0.0, null=True, max_digits=6, decimal_places=2)),
            ('total_pendiente', self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=6, decimal_places=2)),
            ('fecha_apertura', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('fecha_cierre', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'facturas', ['factura'])

        # Adding model 'producto_factura'
        db.create_table(u'facturas_producto_factura', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('factura', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['facturas.factura'])),
            ('producto_precio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inventario.producto_precio'])),
            ('cantidad', self.gf('django.db.models.fields.IntegerField')()),
            ('subtotal', self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=6, decimal_places=2)),
        ))
        db.send_create_signal(u'facturas', ['producto_factura'])

        # Adding model 'abono_factura'
        db.create_table(u'facturas_abono_factura', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('factura', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['facturas.factura'])),
            ('abono', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2)),
            ('fecha_cierre', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'facturas', ['abono_factura'])


    def backwards(self, orm):
        # Deleting model 'impuesto'
        db.delete_table(u'facturas_impuesto')

        # Deleting model 'descuento'
        db.delete_table(u'facturas_descuento')

        # Deleting model 'factura'
        db.delete_table(u'facturas_factura')

        # Deleting model 'producto_factura'
        db.delete_table(u'facturas_producto_factura')

        # Deleting model 'abono_factura'
        db.delete_table(u'facturas_abono_factura')


    models = {
        u'clientes.cliente': {
            'Meta': {'object_name': 'cliente'},
            'celular': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'correo': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '70'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'facturas.abono_factura': {
            'Meta': {'object_name': 'abono_factura'},
            'abono': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'factura': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['facturas.factura']"}),
            'fecha_cierre': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'facturas.descuento': {
            'Meta': {'object_name': 'descuento'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identificador': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'valor_decimal': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'})
        },
        u'facturas.factura': {
            'Meta': {'object_name': 'factura'},
            'cliente': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['clientes.cliente']"}),
            'descuento': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'null': 'True', 'max_digits': '6', 'decimal_places': '2'}),
            'detalles': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'enviada': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'estado': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'fecha_apertura': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'fecha_cierre': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'impuesto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['facturas.impuesto']", 'null': 'True', 'blank': 'True'}),
            'metodo_pago': ('django.db.models.fields.IntegerField', [], {'default': '6'}),
            'saldo_utilizado': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'null': 'True', 'max_digits': '6', 'decimal_places': '2'}),
            'subtotal_factura': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '6', 'decimal_places': '2'}),
            'total_abonado': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'null': 'True', 'max_digits': '6', 'decimal_places': '2'}),
            'total_factura': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '6', 'decimal_places': '2'}),
            'total_pendiente': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '6', 'decimal_places': '2'})
        },
        u'facturas.impuesto': {
            'Meta': {'object_name': 'impuesto'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identificador': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'valor_decimal': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'})
        },
        u'facturas.producto_factura': {
            'Meta': {'object_name': 'producto_factura'},
            'cantidad': ('django.db.models.fields.IntegerField', [], {}),
            'factura': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['facturas.factura']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'producto_precio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inventario.producto_precio']"}),
            'subtotal': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '6', 'decimal_places': '2'})
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