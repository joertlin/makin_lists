# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checklist', '0008_remove_listcontent_item_quantity'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listcontent',
            old_name='item_quantity_num',
            new_name='item_quantity',
        ),
    ]
