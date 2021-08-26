# Generated by Django 3.2.4 on 2021-08-24 15:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0002_ticket_user_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='user_data',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
