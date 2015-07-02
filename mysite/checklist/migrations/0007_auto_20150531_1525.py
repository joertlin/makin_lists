# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checklist', '0006_auto_20150531_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listcontent',
            name='unit_name',
            field=models.ForeignKey(default=1, to='checklist.Unit'),
        ),
    ]
