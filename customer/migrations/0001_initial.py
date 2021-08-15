# Generated by Django 3.2.3 on 2021-08-15 13:58

from django.db import migrations, models
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalOrder',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=255)),
                ('customer_phone', models.CharField(max_length=15)),
                ('amount', models.PositiveIntegerField(default=0)),
                ('order_status', models.CharField(blank=True, max_length=40, null=True)),
                ('order_finished', models.BooleanField(default=False)),
                ('order_rejected', models.BooleanField(default=False)),
                ('booking_time', models.DateTimeField(blank=True, editable=False)),
                ('et_finish', models.PositiveIntegerField(default=0)),
                ('at_finish', models.PositiveIntegerField(default=0)),
                ('et_order', models.PositiveIntegerField(default=0)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
            ],
            options={
                'verbose_name': 'historical order',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalUserRatings',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('rating', models.PositiveSmallIntegerField()),
                ('review', models.TextField(blank=True, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
            ],
            options={
                'verbose_name': 'historical user ratings',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=255)),
                ('customer_phone', models.CharField(max_length=15)),
                ('amount', models.PositiveIntegerField(default=0)),
                ('order_status', models.CharField(blank=True, max_length=40, null=True)),
                ('order_finished', models.BooleanField(default=False)),
                ('order_rejected', models.BooleanField(default=False)),
                ('booking_time', models.DateTimeField(auto_now_add=True)),
                ('et_finish', models.PositiveIntegerField(default=0)),
                ('at_finish', models.PositiveIntegerField(default=0)),
                ('et_order', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='UserRatings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveSmallIntegerField()),
                ('review', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'User Ratings',
            },
        ),
    ]
