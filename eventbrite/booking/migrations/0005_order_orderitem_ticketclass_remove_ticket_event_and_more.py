# Generated by Django 4.2b1 on 2023-04-30 15:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import event.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('event', '0086_event_image10_event_image6_event_image7_event_image8_and_more'),
        ('booking', '0004_alter_ticket_guest_id_booking'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID', models.IntegerField(default=event.models.generate_unique_id, unique=True)),
                ('full_price', models.DecimalField(decimal_places=2, max_digits=8, null=True)),
                ('fee', models.DecimalField(decimal_places=2, max_digits=8, null=True)),
                ('total', models.DecimalField(decimal_places=2, max_digits=8, null=True)),
                ('is_validated', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID', models.IntegerField(default=event.models.generate_unique_id, unique=True)),
                ('quantity', models.PositiveIntegerField()),
                ('ticket_price', models.DecimalField(decimal_places=2, max_digits=8, null=True)),
                ('currency', models.CharField(default='USD', max_length=10)),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='booking.order')),
            ],
        ),
        migrations.CreateModel(
            name='TicketClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID', models.IntegerField(default=event.models.generate_unique_id, unique=True)),
                ('NAME', models.CharField(max_length=20)),
                ('PRICE', models.FloatField()),
                ('EVENT_ID', models.IntegerField()),
                ('GUEST_ID', models.IntegerField(null=True)),
                ('capacity', models.IntegerField()),
                ('quantity_sold', models.IntegerField()),
                ('TICKET_TYPE', models.CharField(choices=[('Free', 'Free'), ('Paid', 'Paid'), ('Donation', 'Donation')], max_length=10)),
                ('Sales_start', models.DateField()),
                ('Sales_end', models.DateField()),
                ('Start_time', models.DateTimeField()),
                ('End_time', models.DateTimeField()),
                ('Absorb_fees', models.CharField(choices=[('True', 'True'), ('False', 'False')], max_length=5)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.event')),
            ],
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='event',
        ),
        migrations.AlterField(
            model_name='discount',
            name='ID',
            field=models.IntegerField(default=event.models.generate_unique_id, unique=True),
        ),
        migrations.AlterField(
            model_name='discount',
            name='percent_off',
            field=models.IntegerField(),
        ),
        migrations.DeleteModel(
            name='Booking',
        ),
        migrations.DeleteModel(
            name='Ticket',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='ticket_class',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.ticketclass'),
        ),
        migrations.AddField(
            model_name='order',
            name='discount',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='booking.discount'),
        ),
        migrations.AddField(
            model_name='order',
            name='event',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='event.event'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]