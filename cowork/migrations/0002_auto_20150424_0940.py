# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cowork', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='office',
            name='price',
            field=models.DecimalField(default=0, max_digits=12, decimal_places=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='room',
            name='price',
            field=models.DecimalField(default=0, max_digits=12, decimal_places=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='desk',
            name='price',
            field=models.DecimalField(max_digits=12, decimal_places=2),
        ),
    ]
