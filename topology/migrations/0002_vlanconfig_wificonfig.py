# Generated by Django 4.2.4 on 2023-08-30 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topology', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VlanConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vlan_name', models.TextField()),
                ('host', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='WifiConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wifi_num', models.IntegerField()),
                ('printer_num', models.IntegerField()),
                ('devices_num', models.IntegerField()),
            ],
        ),
    ]
