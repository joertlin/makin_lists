# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checklist', '0003_auto_20150530_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listcontent',
            name='list_id',
            field=models.ForeignKey(to='checklist.Checklist', db_column=b'list_id'),
        ),
    ]
