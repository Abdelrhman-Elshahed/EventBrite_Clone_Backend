# Generated by Django 4.2b1 on 2023-05-08 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_alter_ticketclass_end_time_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='discount',
            name='percent_off',
        ),
        migrations.AddField(
            model_name='discount',
            name='Discount_price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='discount',
            name='Discountـpercentage',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='discount',
            name='Ends',
            field=models.CharField(choices=[('True', 'True'), ('False', 'False')], default='now', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='discount',
            name='Limitedamount',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='discount',
            name='Reveal_hidden',
            field=models.CharField(choices=[('True', 'True'), ('False', 'False')], default='False', max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='discount',
            name='Starts',
            field=models.CharField(choices=[('True', 'True'), ('False', 'False')], default='now', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='discount',
            name='Ticket_limit',
            field=models.CharField(choices=[('Limited', 'Limited'), ('Unlimited', 'Unlimited')], default='Unlimited', max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='discount',
            name='start_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='discount',
            name='EVENT_ID',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='discount',
            name='Quantity_available',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='discount',
            name='end_date',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='discount',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]