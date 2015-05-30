# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checklist', '0002_auto_20150530_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checklist',
            name='date_completed',
            field=models.DateTimeField(null=True, verbose_name=b'date list was completed', blank=True),
        ),
        migrations.AlterField(
            model_name='listcontent',
            name='date_checked_off',
            field=models.DateTimeField(null=True, verbose_name=b'date item was checked off', blank=True),
        ),
        migrations.AlterField(
            model_name='listitem',
            name='item_name',
            field=models.CharField(max_length=20),
        ),
    ]
