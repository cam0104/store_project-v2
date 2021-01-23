# Generated by Django 2.2 on 2021-01-23 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_project_app', '0017_auto_20210121_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='descripcion',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='venta',
            name='fecha_venta',
            field=models.DateField(default='2021-01-23'),
        ),
    ]
