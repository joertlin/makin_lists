# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checklist', '0004_listcontent_item_unit'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listcontent',
            old_name='item_unit',
            new_name='unit_id',
        ),
    ]
