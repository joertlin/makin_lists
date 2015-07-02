# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checklist', '0005_auto_20150531_1521'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listcontent',
            old_name='unit_id',
            new_name='unit_name',
        ),
    ]
