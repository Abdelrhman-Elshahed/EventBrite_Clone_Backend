# Generated by Django 4.2b1 on 2023-04-26 06:13

from django.db import migrations, models
import event.models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0067_alter_event_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='ID',
            field=models.IntegerField(default=event.models.generate_unique_id, unique=True),
        ),
    ]