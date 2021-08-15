# Generated by Django 3.2.3 on 2021-07-30 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopadmin', '0009_auto_20210730_2126'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalsubservice',
            name='shops',
        ),
        migrations.RemoveField(
            model_name='subservice',
            name='shops',
        ),
        migrations.AddField(
            model_name='subservice',
            name='shops',
            field=models.ManyToManyField(to='shopadmin.ShopBranch'),
        ),
    ]
