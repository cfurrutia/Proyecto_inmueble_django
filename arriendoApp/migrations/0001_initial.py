# Generated by Django 5.0.6 on 2024-07-09 02:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TipoInmueble',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='TipoUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Inmueble',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('m2_construidos', models.IntegerField()),
                ('m2_totales', models.IntegerField()),
                ('estacionamientos', models.IntegerField()),
                ('habitaciones', models.IntegerField()),
                ('banos', models.IntegerField()),
                ('direccion', models.CharField(max_length=200)),
                ('precio_mensual', models.IntegerField()),
                ('comuna', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arriendoApp.comuna')),
                ('tipo_inmueble', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arriendoApp.tipoinmueble')),
            ],
        ),
        migrations.AddField(
            model_name='comuna',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arriendoApp.region'),
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('tipo_usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='arriendoApp.tipousuario')),
            ],
        ),
        migrations.CreateModel(
            name='ContratoArriendo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField(blank=True, null=True)),
                ('estado', models.CharField(default='ACTIVO', max_length=20)),
                ('inmueble', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arriendoApp.inmueble')),
                ('arrendador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contratos_arrendador', to='arriendoApp.usuario')),
                ('arrendatario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contratos_arrendatario', to='arriendoApp.usuario')),
            ],
        ),
    ]
