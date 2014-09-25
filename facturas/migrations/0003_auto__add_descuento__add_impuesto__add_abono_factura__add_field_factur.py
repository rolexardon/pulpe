# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'descuento'
        db.create_table(u'facturas_descuento', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('identificador', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('valor_decimal', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2)),
        ))
        db.send_create_signal(u'facturas', ['descuento'])

        # Adding model 'impuesto'
        db.create_table(u'facturas_impuesto', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('identificador', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('valor_decimal', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2)),
        ))
        db.send_create_signal(u'facturas', ['impuesto'])

        # Adding model 'abono_factura'
        db.create_table(u'facturas_abono_factura', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('factura', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['facturas.factura'])),
            ('abono', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2)),
            ('fecha_cierre', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'facturas', ['abono_factura'])

        # Adding field 'factura.impuesto'
        db.add_column(u'facturas_factura', 'impuesto',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['facturas.impuesto']),
                      keep_default=False)

        # Adding field 'factura.descuento'
        db.add_column(u'facturas_factura', 'descuento',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['facturas.descuento']),
                      keep_default=False)

        # Adding field 'factura.saldo_utilizado'
        db.add_column(u'facturas_factura', 'saldo_utilizado',
                      self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=6, decimal_places=2),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'descuento'
        db.delete_table(u'facturas_descuento')

        # Deleting model 'impuesto'
        db.delete_table(u'facturas_impuesto')

        # Deleting model 'abono_factura'
        db.delete_table(u'facturas_abono_factura')

        # Deleting field 'factura.impuesto'
        db.delete_column(u'facturas_factura', 'impuesto_id')

        # Deleting field 'factura.descuento'
        db.delete_column(u'facturas_factura', 'descuento_id')

        # Deleting field 'factura.saldo_utilizado'
        db.delete_column(u'facturas_factura', 'saldo_utilizado')


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
            'descuento': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['facturas.descuento']"}),
            'estado': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'fecha_apertura': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'fecha_cierre': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'impuesto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['facturas.impuesto']"}),
            'saldo_utilizado': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '6', 'decimal_places': '2'}),
            'total_abonado': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '6', 'decimal_places': '2'}),
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