# Generated by Django 4.2b1 on 2023-03-21 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0010_rename_name_event_title_rename_type_event_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='Category',
            field=models.CharField(default='string', max_length=10),
            preserve_default=False,
        ),
    ]