# Generated by Django 4.0.4 on 2022-06-20 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema_2', '0004_alter_clientes_cli_ruc'),
    ]

    operations = [
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pro_nombre', models.CharField(max_length=64)),
                ('pro_codigo', models.CharField(max_length=64)),
                ('pro_categoria', models.CharField(max_length=64)),
                ('pro_sub_categoria', models.CharField(max_length=64)),
                ('pro_unidad_med', models.CharField(max_length=64, null=True)),
                ('pro_precio_compra_sin_igv', models.FloatField()),
                ('pro_precio_compra_con_igv', models.FloatField()),
                ('pro_precio_venta_sin_igv', models.FloatField()),
                ('pro_precio_venta_con_igv', models.FloatField()),
                ('pro_codigo_sunat', models.CharField(max_length=64, null=True)),
                ('pro_descuento', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Servicios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ser_nombre', models.CharField(max_length=64)),
                ('ser_categoria', models.CharField(max_length=64)),
                ('ser_sub_categoria', models.CharField(max_length=64)),
                ('ser_unidad_med', models.CharField(max_length=64)),
                ('ser_precio_venta_sin_igv', models.FloatField()),
                ('ser_precio_venta_con_igv', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usr_usuario', models.CharField(max_length=64)),
                ('usr_password', models.CharField(max_length=64)),
                ('usr_email', models.CharField(max_length=64)),
            ],
        ),
    ]