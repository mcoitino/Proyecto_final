# Generated by Django 4.1.7 on 2023-06-28 18:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Preentrega3App', '0014_remove_userprofile_link_web'),
    ]

    operations = [
        migrations.AddField(
            model_name='sobrenosotros',
            name='fecha_creado',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='link_web',
            field=models.URLField(default=''),
        ),
    ]
