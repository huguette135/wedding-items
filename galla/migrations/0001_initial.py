# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-02-11 03:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(null=True, upload_to='photos/')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(max_length=400)),
                ('category', models.ForeignKey(blank=True, null='True', on_delete=django.db.models.deletion.CASCADE, to='galla.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.AddField(
            model_name='image',
            name='location',
            field=models.ForeignKey(blank=True, null='True', on_delete=django.db.models.deletion.CASCADE, to='galla.Location'),
        ),
    ]
