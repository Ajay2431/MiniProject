# Generated by Django 4.1 on 2023-07-03 08:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seminardetails', '0003_alter_batch_deactivation_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batch',
            name='deactivation_date',
            field=models.DateField(default=datetime.datetime(2023, 12, 30, 8, 50, 59, 457483)),
        ),
    ]
