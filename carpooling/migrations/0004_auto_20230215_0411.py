# Generated by Django 3.2.16 on 2023-02-15 04:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('carpooling', '0003_auto_20230214_2131'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trip',
            name='destination_lat',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='trip',
            name='destination_lon',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='trip',
            name='origin_lat',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='trip',
            name='origin_lon',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='trip',
            name='role',
            field=models.CharField(choices=[('driver', 'driver'), ('passenger', 'passenger')], max_length=10),
        ),
        migrations.AlterField(
            model_name='trip',
            name='status',
            field=models.CharField(choices=[('active', 'active'), ('ended', 'ended')], default='active', max_length=10),
        ),
    ]