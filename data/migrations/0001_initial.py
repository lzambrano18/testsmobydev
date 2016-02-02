# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cause',
            fields=[
                ('id', models.AutoField(
                    verbose_name='ID',
                    auto_created=True,
                    serialize=False,
                    primary_key=True)),
                ('year', models.CharField(max_length=4)),
                ('ethnicity', models.CharField(max_length=200)),
                ('sex', models.CharField(max_length=6)),
                ('cause_of_death', models.CharField(max_length=200)),
                ('count', models.IntegerField()),
                ('percent', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
