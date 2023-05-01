# Generated by Django 4.2b1 on 2023-04-28 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventManagment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publish_info',
            name='Audience_Link',
            field=models.CharField(default='', editable=False, max_length=50),
        ),
        migrations.AlterField(
            model_name='publish_info',
            name='Audience_Password',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='publish_info',
            name='Keep_Private',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='publish_info',
            name='Publication_Date',
            field=models.DateField(blank=True, default='2023-04-01'),
            preserve_default=False,
        ),
    ]