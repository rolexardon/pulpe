# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facturas', '0003_factura_otros_cargos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='factura',
            name='total_factura',
        ),
    ]
