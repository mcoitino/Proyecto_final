# Generated by Django 4.1.7 on 2023-06-29 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Preentrega3App', '0018_alter_avatar_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avatar',
            name='image',
            field=models.ImageField(blank=True, default='avatares/avatar_pred.png', null=True, upload_to='es'),
        ),
    ]
