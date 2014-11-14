# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facturas', '0002_auto_20141020_1610'),
    ]

    operations = [
        migrations.AddField(
            model_name='factura',
            name='otros_cargos',
            field=models.DecimalField(default=0.0, null=True, max_digits=6, decimal_places=2),
            preserve_default=True,
        ),
    ]
