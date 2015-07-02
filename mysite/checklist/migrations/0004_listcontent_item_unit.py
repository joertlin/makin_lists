# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checklist', '0003_auto_20150531_1512'),
    ]

    operations = [
        migrations.AddField(
            model_name='listcontent',
            name='item_unit',
            field=models.ForeignKey(to='checklist.Unit', null=True),
        ),
    ]
