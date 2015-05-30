# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checklist', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllItems',
            fields=[
                ('item_id', models.AutoField(serialize=False, primary_key=True)),
                ('item_name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='ListItems',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item_quantity', models.CharField(max_length=10)),
                ('date_checked_off', models.DateTimeField(null=True, verbose_name=b'date item was checked off')),
                ('item_id', models.ManyToManyField(to='checklist.AllItems')),
            ],
        ),
        migrations.RenameModel(
            old_name='check_lists',
            new_name='Checklist',
        ),
        migrations.AddField(
            model_name='listitems',
            name='list_id',
            field=models.ForeignKey(to='checklist.Checklist'),
        ),
    ]
