# Generated by Django 5.1.3 on 2024-12-10 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sicp', '0002_personaproteccion_telefono'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personaproteccion',
            name='nuip',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='personaproteccion',
            name='telefono',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]