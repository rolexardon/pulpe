
# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'cliente.cargo'
        db.delete_column(u'clientes_cliente', 'cargo')

        # Deleting field 'cliente.apellido'
        db.delete_column(u'clientes_cliente', 'apellido')


    def backwards(self, orm):
        # Adding field 'cliente.cargo'
        db.add_column(u'clientes_cliente', 'cargo',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=150),
                      keep_default=False)

        # Adding field 'cliente.apellido'
        db.add_column(u'clientes_cliente', 'apellido',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=250),
                      keep_default=False)


    models = {
        u'clientes.cliente': {
            'Meta': {'object_name': 'cliente'},
            'celular': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'correo': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '70'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'clientes.saldo_cliente': {
            'Meta': {'object_name': 'saldo_cliente'},
            'cliente': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['clientes.cliente']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'saldo': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'})
        }
    }

    complete_apps = ['clientes']