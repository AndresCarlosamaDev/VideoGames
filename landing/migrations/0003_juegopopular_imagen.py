# Generated by Django 4.1.7 on 2023-03-21 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0002_juegopopular_alter_usuario_correo'),
    ]

    operations = [
        migrations.AddField(
            model_name='juegopopular',
            name='imagen',
            field=models.ImageField(null=True, upload_to='../landing/static/images'),
        ),
    ]
