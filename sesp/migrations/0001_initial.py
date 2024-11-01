# Generated by Django 5.1.2 on 2024-11-01 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DatosSesp',
            fields=[
                ('serial', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=15, null=True)),
                ('departamento', models.CharField(blank=True, max_length=100, null=True)),
                ('ciudad', models.CharField(blank=True, max_length=100, null=True)),
                ('mtsp', models.CharField(blank=True, max_length=20, null=True)),
                ('nivel_riesgo', models.CharField(blank=True, max_length=30, null=True)),
                ('telefono_contacto', models.CharField(blank=True, max_length=15, null=True)),
            ],
        ),
    ]
