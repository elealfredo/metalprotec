# Generated by Django 4.0.4 on 2022-06-29 18:12

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema_2', '0031_guias_gui_codigo_alter_guias_gui_estado_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='guias',
            name='gui_descuentos',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(default=0), null=True, size=None),
        ),
    ]
