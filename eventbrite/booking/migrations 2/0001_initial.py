# Generated by Django 4.2b1 on 2023-05-01 23:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import event.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('event', '0088_event_image1_alter_event_image_alter_event_image2_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID', models.IntegerField(default=event.models.generate_unique_id, unique=True)),
                ('EVENT_ID', models.IntegerField(default=11111)),
                ('percent_off', models.IntegerField()),
                ('CODE', models.CharField(max_length=20)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('Quantity_available', models.IntegerField()),
                ('User_ID', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID', models.IntegerField(default=event.models.generate_unique_id, unique=True)),
                ('full_price', models.FloatField(null=True)),
                ('fee', models.FloatField(null=True)),
                ('total', models.FloatField(null=True)),
                ('is_validated', models.BooleanField(default=False)),
                ('discount', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='booking.discount')),
                ('event', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='event.event')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TicketClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID', models.IntegerField(default=event.models.generate_unique_id, unique=True)),
                ('EVENT_ID', models.IntegerField()),
                ('User_id', models.IntegerField(blank=True, null=True)),
                ('NAME', models.CharField(blank=True, max_length=20, null=True)),
                ('PRICE', models.FloatField()),
                ('capacity', models.IntegerField()),
                ('quantity_sold', models.IntegerField()),
                ('TICKET_TYPE', models.CharField(blank=True, choices=[('Free', 'Free'), ('Paid', 'Paid'), ('Donation', 'Donation')], max_length=10, null=True)),
                ('Sales_start', models.DateField()),
                ('Sales_end', models.DateField()),
                ('Start_time', models.DateTimeField()),
                ('End_time', models.DateTimeField()),
                ('Absorb_fees', models.CharField(choices=[('True', 'True'), ('False', 'False')], max_length=5)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.event')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('ID', models.IntegerField(default=event.models.generate_unique_id, unique=True)),
                ('quantity', models.PositiveIntegerField()),
                ('ticket_price', models.FloatField(null=True)),
                ('currency', models.CharField(default='USD', max_length=10)),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='booking.order')),
                ('ticket_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.ticketclass')),
            ],
        ),
    ]