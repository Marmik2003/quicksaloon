# Generated by Django 3.2.3 on 2021-08-14 13:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0004_auto_20210727_2113'),
        ('customer', '0005_auto_20210814_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='barber',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='public.barber'),
        ),
    ]
