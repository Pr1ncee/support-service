# Generated by Django 3.2.4 on 2021-08-30 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_answer_date_added'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='status',
            field=models.CharField(default='unsolved', max_length=8),
        ),
    ]
