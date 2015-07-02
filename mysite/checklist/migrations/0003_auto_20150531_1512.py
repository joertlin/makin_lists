# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checklist', '0002_unit'),
    ]

    operations = [
        migrations.AddField(
            model_name='listcontent',
            name='item_quantity_num',
            field=models.FloatField(default=1, verbose_name=b'number of units'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='listcontent',
            name='item_quantity',
            field=models.CharField(max_length=10, verbose_name=b'number of units'),
        ),
    ]
