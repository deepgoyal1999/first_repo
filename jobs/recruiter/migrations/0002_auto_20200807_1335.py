# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-08-07 08:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruiter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='delhijobinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('cname', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=30)),
                ('phonenum', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='hydjobinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('cname', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=30)),
                ('phonenum', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='mumbaijobinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('cname', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=30)),
                ('phonenum', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='jobinfo',
        ),
    ]