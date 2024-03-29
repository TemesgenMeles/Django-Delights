# Generated by Django 5.0.2 on 2024-03-17 07:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_alter_purchase_menu_item'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cost', models.FloatField(default=0)),
                ('Revenue', models.FloatField(default=0)),
                ('Profit', models.FloatField(default=0)),
                ('Timestamp_start', models.DateTimeField()),
                ('Timestamp_end', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='PurcahseHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Menu_name', models.CharField(max_length=50)),
                ('Timestamp', models.DateTimeField()),
                ('Quantity', models.IntegerField(default=1)),
                ('Total_price', models.FloatField()),
            ],
        ),
        migrations.AlterField(
            model_name='purchase',
            name='Menu_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventory.menuitem', verbose_name='Menu Item'),
        ),
    ]
