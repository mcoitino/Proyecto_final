# Generated by Django 4.1.7 on 2023-06-27 19:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Preentrega3App', '0005_playas_fecha_creado_playas_usuario_creacion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='senderismo',
            name='usuario_creacion',
            field=models.CharField(default='??', max_length=20),
        ),
        migrations.CreateModel(
            name='Imagen_usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='avatar')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
