# Generated by Django 4.0.4 on 2022-06-26 19:32

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema_2', '0015_remove_proformas_prof_cantidad_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Facturas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fac_cliente', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=64), size=None)),
                ('fac_fecha', models.CharField(max_length=64)),
                ('fac_valor_total', models.FloatField()),
                ('fac_estado', models.CharField(max_length=64)),
                ('fac_productos', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=64), size=None)),
            ],
        ),
        migrations.CreateModel(
            name='Guias',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('gui_cliente', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=64), size=None)),
                ('gui_fecha', models.CharField(max_length=64)),
                ('gui_valor_total', models.FloatField()),
                ('gui_estado', models.CharField(max_length=64)),
                ('gui_productos', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=64), size=None)),
            ],
        ),
    ]
