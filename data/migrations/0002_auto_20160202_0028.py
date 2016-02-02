# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from data.models import Cause
from django.db import migrations, models


def MigrateDataAll(apps, schema_editor):

    with open("rows.json") as json_file:
        json_data = json.load(json_file)

        rows = []
        for row in json_data['data']:
            cause = Cause(
                percent=row[13],
                count=row[12],
                cause_of_death=row[11],
                sex=row[10],
                ethnicity=row[9],
                year=row[8],
            )
            rows.append(cause)
        Cause.objects.bulk_create(rows)


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(MigrateDataAll),
    ]
