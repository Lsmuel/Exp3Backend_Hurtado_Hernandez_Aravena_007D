# Generated by Django 3.2.3 on 2021-06-21 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extension', '0004_ropa_zapatillas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ropa',
            name='tallaRopa',
            field=models.CharField(max_length=5, verbose_name='Talla Ropa'),
        ),
    ]
