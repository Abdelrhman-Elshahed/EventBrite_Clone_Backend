# Generated by Django 4.2b1 on 2023-04-14 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0037_event_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(upload_to='events/'),
        ),
    ]