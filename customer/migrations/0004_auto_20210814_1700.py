# Generated by Django 3.2.3 on 2021-08-14 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_auto_20210814_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicaluserratings',
            name='review',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userratings',
            name='review',
            field=models.TextField(blank=True, null=True),
        ),
    ]
