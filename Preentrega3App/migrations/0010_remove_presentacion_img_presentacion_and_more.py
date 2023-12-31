# Generated by Django 4.1.7 on 2023-06-28 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Preentrega3App', '0009_senderismo_usuario_autorizado_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='presentacion',
            name='img_presentacion',
        ),
        migrations.RemoveField(
            model_name='senderismo',
            name='usuario_autorizado',
        ),
        migrations.AddField(
            model_name='presentacion',
            name='img_senderismo',
            field=models.ImageField(blank=True, upload_to='imagenes/'),
        ),
        migrations.AlterField(
            model_name='playas',
            name='img_playa',
            field=models.ImageField(blank=True, upload_to='imagenes/'),
        ),
        migrations.AlterField(
            model_name='pueblos',
            name='img_pueblo',
            field=models.ImageField(blank=True, upload_to='imagenes/'),
        ),
    ]
