# Generated by Django 4.2.4 on 2023-08-15 11:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seminardetails', '0004_alter_batch_deactivation_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='BatchUserMapping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=130)),
                ('username', models.CharField(max_length=30)),
            ],
        ),
        migrations.RenameField(
            model_name='seminar',
            old_name='batch_id',
            new_name='batch',
        ),
        migrations.RenameField(
            model_name='seminar',
            old_name='author',
            new_name='created_by',
        ),
        migrations.AddField(
            model_name='seminar',
            name='other_link',
            field=models.URLField(default=False, max_length=250),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='batch',
            name='deactivation_date',
            field=models.DateField(default=datetime.datetime(2024, 2, 11, 11, 38, 33, 365849)),
        ),
    ]
