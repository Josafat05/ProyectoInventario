# Generated by Django 5.1.4 on 2025-03-07 20:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoreo', '0002_authgroup_authgrouppermissions_authpermission_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rutas',
            fields=[
                ('id_ruta', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_ruta', models.CharField(max_length=255)),
                ('descripcion', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'rutas',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='MonitoreoDispositivo',
        ),
        migrations.CreateModel(
            name='RutaDispositivos',
            fields=[
                ('id_ruta', models.OneToOneField(db_column='id_ruta', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='monitoreo.rutas')),
                ('orden', models.IntegerField()),
            ],
            options={
                'db_table': 'ruta_dispositivos',
                'managed': False,
            },
        ),
    ]
