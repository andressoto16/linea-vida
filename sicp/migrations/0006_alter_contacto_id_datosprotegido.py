# Generated by Django 5.1.3 on 2024-12-10 16:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sicp', '0005_alter_vehiculo_color_alter_vehiculo_marca_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacto',
            name='id_datosprotegido',
            field=models.ForeignKey(blank=True, db_column='id_datosprotegido', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='contactos', to='sicp.datosprotegido'),
        ),
    ]
