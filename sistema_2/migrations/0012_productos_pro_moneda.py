# Generated by Django 4.0.4 on 2022-06-22 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema_2', '0011_alter_clientes_cli_razon_social'),
    ]

    operations = [
        migrations.AddField(
            model_name='productos',
            name='pro_moneda',
            field=models.CharField(max_length=64, null=True),
        ),
    ]
