# Generated by Django 4.1.7 on 2023-07-01 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Preentrega3App', '0026_alter_avatar_image_alter_userprofile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, default='', null=True, upload_to='imagenes'),
        ),
    ]
