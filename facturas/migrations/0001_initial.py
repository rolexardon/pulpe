# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '__first__'),
        ('clientes', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='abono_factura',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('abono', models.DecimalField(max_digits=6, decimal_places=2)),
                ('fecha_cierre', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='descuento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('identificador', models.CharField(max_length=4)),
                ('valor_decimal', models.DecimalField(max_digits=6, decimal_places=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='factura',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('estado', models.IntegerField(default=1, choices=[(1, b'PENDIENTE'), (2, b'PAGADA')])),
                ('metodo_pago', models.IntegerField(default=6, choices=[(1, b'TIGOMONEY'), (2, b'BAC'), (3, b'FICOHSA'), (4, b'ATLANTIDA'), (5, b'OCCIDENTE'), (6, b'EFECTIVO')])),
                ('detalles', models.TextField(null=True, blank=True)),
                ('enviada', models.BooleanField(default=False)),
                ('descuento', models.DecimalField(default=0.0, null=True, max_digits=6, decimal_places=2)),
                ('saldo_utilizado', models.DecimalField(default=0.0, null=True, max_digits=6, decimal_places=2)),
                ('subtotal_factura', models.DecimalField(default=0.0, max_digits=6, decimal_places=2)),
                ('total_factura', models.DecimalField(default=0.0, max_digits=6, decimal_places=2)),
                ('total_abonado', models.DecimalField(default=0.0, null=True, max_digits=6, decimal_places=2)),
                ('total_pendiente', models.DecimalField(default=0.0, max_digits=6, decimal_places=2)),
                ('fecha_apertura', models.DateField(auto_now_add=True)),
                ('fecha_cierre', models.DateField(null=True, blank=True)),
                ('cliente', models.ForeignKey(to='clientes.cliente')),
            ],
            options={
                'ordering': ['-fecha_apertura', 'cliente__nombre'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='impuesto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('identificador', models.CharField(max_length=4)),
                ('valor_decimal', models.DecimalField(max_digits=6, decimal_places=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='producto_factura',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.IntegerField()),
                ('subtotal', models.DecimalField(default=0.0, max_digits=6, decimal_places=2)),
                ('factura', models.ForeignKey(to='facturas.factura')),
                ('producto_precio', models.ForeignKey(to='inventario.producto_precio')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='factura',
            name='impuesto',
            field=models.ForeignKey(blank=True, to='facturas.impuesto', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='abono_factura',
            name='factura',
            field=models.ForeignKey(to='facturas.factura'),
            preserve_default=True,
        ),
    ]
