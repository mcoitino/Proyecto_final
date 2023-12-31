# Generated by Django 4.1.7 on 2023-06-27 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Preentrega3App', '0007_imagenes_delete_imagen_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='playas',
            name='img_playa',
            field=models.ImageField(blank=True, upload_to='', verbose_name='imagenes/'),
        ),
        migrations.AddField(
            model_name='presentacion',
            name='img_presentacion',
            field=models.ImageField(blank=True, upload_to='', verbose_name='imagenes/'),
        ),
        migrations.AddField(
            model_name='pueblos',
            name='img_pueblo',
            field=models.ImageField(blank=True, upload_to='', verbose_name='imagenes/'),
        ),
        migrations.AddField(
            model_name='senderismo',
            name='img_senderismo',
            field=models.ImageField(blank=True, upload_to='', verbose_name='imagenes/'),
        ),
        migrations.DeleteModel(
            name='Imagenes',
        ),
    ]
