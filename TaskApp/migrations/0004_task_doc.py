# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-20 09:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TaskApp', '0003_task_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='doc',
            field=models.FileField(default='Doc/None/No-doc.pdf', upload_to='Doc/'),
        ),
    ]