# Generated by Django 4.0.4 on 2022-06-27 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema_2', '0018_alter_facturas_fac_productos_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='proformas',
            name='prof_vendedor',
            field=models.CharField(max_length=64, null=True),
        ),
    ]