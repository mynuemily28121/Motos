# Generated by Django 5.0 on 2023-12-10 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moto',
            name='imagen',
            field=models.ImageField(upload_to='motos'),
        ),
    ]
