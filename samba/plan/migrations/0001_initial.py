# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-07 19:39
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('geo', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Aquisicao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plugin', models.CharField(max_length=100, verbose_name='nome')),
            ],
            options={
                'verbose_name_plural': 'aquisições',
                'verbose_name': 'aquisição',
            },
        ),
        migrations.CreateModel(
            name='Indicador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sigla', models.CharField(max_length=20, verbose_name='sigla')),
                ('valor', models.CharField(max_length=200, verbose_name='valor')),
                ('descricao', models.TextField(blank=True, verbose_name='descrição do valor do indicador')),
            ],
            options={
                'verbose_name_plural': 'valores dos indicadores',
                'verbose_name': 'valor do indicador',
            },
        ),
        migrations.CreateModel(
            name='Plano',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano', models.IntegerField(default=2016, verbose_name='ano')),
                ('dono', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='dono')),
                ('municipio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='geo.Municipio', verbose_name='município')),
            ],
            options={
                'verbose_name_plural': 'planos',
                'verbose_name': 'plano',
            },
        ),
        migrations.AddField(
            model_name='indicador',
            name='plano',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plan.Plano', verbose_name='plano'),
        ),
        migrations.AddField(
            model_name='aquisicao',
            name='plano',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plan.Plano', verbose_name='plano'),
        ),
    ]
