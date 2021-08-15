# Generated by Django 3.2.3 on 2021-07-27 15:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0003_alter_user_last_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='barber',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='historicalbarber',
            name='id',
            field=models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='barber',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
