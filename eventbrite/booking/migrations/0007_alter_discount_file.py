# Generated by Django 4.2b1 on 2023-05-08 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0006_discount_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discount',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='csv/'),
        ),
    ]
