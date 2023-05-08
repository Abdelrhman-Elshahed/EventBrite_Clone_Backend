# Generated by Django 4.2b1 on 2023-05-08 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_alter_discount_reveal_hidden_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discount',
            name='Ends',
            field=models.CharField(blank=True, choices=[('True', 'True'), ('False', 'False')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='discount',
            name='Starts',
            field=models.CharField(blank=True, choices=[('True', 'True'), ('False', 'False')], max_length=20, null=True),
        ),
    ]
