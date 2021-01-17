# Generated by Django 2.2 on 2021-01-17 20:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store_project_app', '0010_auto_20210114_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='genero',
            field=models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], default=None, max_length=10, verbose_name='Genero'),
        ),
        migrations.AlterField(
            model_name='metodo_pago',
            name='id_metodo_pago',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='venta',
            name='id_cliente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store_project_app.Cliente'),
        ),
    ]
