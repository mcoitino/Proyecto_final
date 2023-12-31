# Generated by Django 4.1.7 on 2023-06-27 20:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Preentrega3App', '0006_alter_senderismo_usuario_creacion_imagen_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Imagenes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='media')),
                ('registro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Imagenes',
            },
        ),
        migrations.DeleteModel(
            name='Imagen_usuario',
        ),
    ]
