# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-20 19:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dopObrazovanieApp', '0002_auto_20160512_2338'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorites',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FavoriteTeacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dopObrazovanieApp.Teacher')),
            ],
        ),
    ]