# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-23 05:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kitchen', '0002_auto_20180323_0349'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='id',
        ),
        migrations.AlterField(
            model_name='student',
            name='student_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]