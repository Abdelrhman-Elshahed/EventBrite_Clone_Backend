# Generated by Django 4.2b1 on 2023-04-26 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0069_alter_eventfollower_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventfollower',
            name='ID',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]