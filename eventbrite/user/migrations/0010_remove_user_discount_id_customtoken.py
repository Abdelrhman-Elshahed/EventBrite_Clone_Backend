# Generated by Django 4.2b1 on 2023-04-28 13:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authtoken', '0003_tokenproxy'),
        ('user', '0009_delete_passwordresettoken'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='DISCOUNT_ID',
        ),
        migrations.CreateModel(
            name='CustomToken',
            fields=[
                ('token_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='authtoken.token')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='custom_tokens', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'CustomToken',
                'verbose_name_plural': 'CustomTokens',
            },
            bases=('authtoken.token',),
        ),
    ]
