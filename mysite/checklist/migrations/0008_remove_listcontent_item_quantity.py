# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checklist', '0007_auto_20150531_1525'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listcontent',
            name='item_quantity',
        ),
    ]
