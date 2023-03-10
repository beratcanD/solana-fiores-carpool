# Generated by Django 3.2.16 on 2023-02-28 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carpooling', '0012_alter_trip_driver'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='passengers',
            field=models.ManyToManyField(blank=True, null=True, related_name='_carpooling_trip_passengers_+', to='carpooling.Trip'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='requests',
            field=models.ManyToManyField(blank=True, null=True, related_name='_carpooling_trip_requests_+', to='carpooling.Trip'),
        ),
    ]
