# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checklist', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('unit_id', models.AutoField(serialize=False, primary_key=True)),
                ('unit_name', models.CharField(max_length=4)),
            ],
        ),
    ]
