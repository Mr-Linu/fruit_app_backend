# Generated by Django 4.2.4 on 2023-08-19 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_appuser_is_verified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Contact',
            field=models.PositiveIntegerField(default=''),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(default='', max_length=255),
        ),
    ]