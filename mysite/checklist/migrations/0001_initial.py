# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Checklist',
            fields=[
                ('list_id', models.AutoField(serialize=False, primary_key=True)),
                ('list_name', models.CharField(max_length=10)),
                ('date_created', models.DateTimeField(verbose_name=b'date list was created')),
                ('date_completed', models.DateTimeField(null=True, verbose_name=b'date list was completed', blank=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ListContent',
            fields=[
                ('content_id', models.AutoField(serialize=False, primary_key=True)),
                ('item_quantity', models.CharField(max_length=10)),
                ('date_checked_off', models.DateTimeField(null=True, verbose_name=b'date item was checked off', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ListItem',
            fields=[
                ('item_id', models.AutoField(serialize=False, primary_key=True)),
                ('item_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='listcontent',
            name='item_id',
            field=models.ManyToManyField(to='checklist.ListItem'),
        ),
        migrations.AddField(
            model_name='listcontent',
            name='list_id',
            field=models.ForeignKey(to='checklist.Checklist', db_column=b'list_id'),
        ),
    ]
