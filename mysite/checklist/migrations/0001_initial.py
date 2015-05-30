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
            name='AllItems',
            fields=[
                ('item_id', models.AutoField(serialize=False, primary_key=True)),
                ('item_name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Checklist',
            fields=[
                ('list_id', models.AutoField(serialize=False, primary_key=True)),
                ('list_name', models.CharField(max_length=10)),
                ('date_created', models.DateTimeField(verbose_name=b'date list was created')),
                ('date_completed', models.DateTimeField(null=True, verbose_name=b'date list was completed')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ListItems',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item_quantity', models.CharField(max_length=10)),
                ('date_checked_off', models.DateTimeField(null=True, verbose_name=b'date item was checked off')),
                ('item_id', models.ManyToManyField(to='checklist.AllItems')),
                ('list_id', models.ForeignKey(to='checklist.Checklist')),
            ],
        ),
    ]
