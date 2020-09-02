# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-09-02 10:06
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('corona', '0005_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]