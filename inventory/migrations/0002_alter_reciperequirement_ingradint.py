# Generated by Django 5.0.2 on 2024-03-16 18:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reciperequirement',
            name='Ingradint',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventory.ingradient', verbose_name='Recipe'),
        ),
    ]
