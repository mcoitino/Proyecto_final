# Generated by Django 4.1.7 on 2023-06-28 09:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Preentrega3App', '0008_playas_img_playa_presentacion_img_presentacion_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='senderismo',
            name='usuario_autorizado',
            field=models.ForeignKey(default=None, limit_choices_to={'is_staff': True}, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='senderismo',
            name='img_senderismo',
            field=models.ImageField(blank=True, upload_to='imagenes/'),
        ),
    ]
