# Generated by Django 4.2b1 on 2023-04-25 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0051_remove_event_images_delete_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='events/')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='images',
            field=models.ManyToManyField(blank=True, related_name='events', to='event.eventimage'),
        ),
    ]