# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'cliente'
        db.create_table(u'clientes_cliente', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('apellido', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('cargo', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('celular', self.gf('django.db.models.fields.CharField')(max_length=8)),
            ('correo', self.gf('django.db.models.fields.EmailField')(unique=True, max_length=70)),
        ))
        db.send_create_signal(u'clientes', ['cliente'])


    def backwards(self, orm):
        # Deleting model 'cliente'
        db.delete_table(u'clientes_cliente')


    models = {
        u'clientes.cliente': {
            'Meta': {'object_name': 'cliente'},
            'apellido': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'cargo': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'celular': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'correo': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '70'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        }
    }

    complete_apps = ['clientes']