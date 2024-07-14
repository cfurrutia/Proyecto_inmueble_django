# Generated by Django 5.0.6 on 2024-07-13 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arriendoapp', '0004_alter_usuario_correo_alter_usuario_rut_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='correo',
        ),
        migrations.AlterField(
            model_name='usuario',
            name='apellidos',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='direccion',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nombres',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='rut',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='telefono',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='tipo_usuario',
            field=models.CharField(choices=[('arrendatario', 'Arrendatario'), ('arrendador', 'Arrendador'), ('ambos', 'Ambos')], default='arrendatario', max_length=20),
        ),
    ]
