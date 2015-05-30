# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checklist', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListContent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item_quantity', models.CharField(max_length=10)),
                ('date_checked_off', models.DateTimeField(null=True, verbose_name=b'date item was checked off')),
            ],
        ),
        migrations.RenameModel(
            old_name='AllItems',
            new_name='ListItem',
        ),
        migrations.RemoveField(
            model_name='listitems',
            name='item_id',
        ),
        migrations.RemoveField(
            model_name='listitems',
            name='list_id',
        ),
        migrations.DeleteModel(
            name='ListItems',
        ),
        migrations.AddField(
            model_name='listcontent',
            name='item_id',
            field=models.ManyToManyField(to='checklist.ListItem'),
        ),
        migrations.AddField(
            model_name='listcontent',
            name='list_id',
            field=models.ForeignKey(to='checklist.Checklist'),
        ),
    ]
