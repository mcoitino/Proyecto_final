# Generated by Django 4.1.7 on 2023-06-27 10:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Preentrega3App', '0002_categorías'),
    ]

    operations = [
        migrations.AddField(
            model_name='pueblos',
            name='fecha_creado',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
