# Generated by Django 4.1.7 on 2023-03-04 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carpooling', '0014_auto_20230228_2052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='passengers',
            field=models.ManyToManyField(blank=True, related_name='passenger_trips', to='carpooling.trip'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='requests',
            field=models.ManyToManyField(blank=True, related_name='requests', to='carpooling.trip'),
        ),
    ]