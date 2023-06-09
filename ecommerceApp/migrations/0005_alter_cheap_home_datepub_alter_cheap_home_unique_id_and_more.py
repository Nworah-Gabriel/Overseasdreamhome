# Generated by Django 4.1.8 on 2023-06-01 00:33

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerceApp', '0004_enquirie_subject_alter_cheap_home_datepub_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cheap_home',
            name='DatePub',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 1, 1, 33, 20, 271230), editable=False, verbose_name='Date Created'),
        ),
        migrations.AlterField(
            model_name='cheap_home',
            name='unique_id',
            field=models.UUIDField(default=uuid.UUID('ae35a0bd-2d22-43a7-b68a-bc6b4fdc46e8'), editable=False),
        ),
        migrations.AlterField(
            model_name='dream_mansion',
            name='DatePub',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 1, 1, 33, 20, 271230), editable=False, verbose_name='Date Created'),
        ),
        migrations.AlterField(
            model_name='dream_mansion',
            name='unique_id',
            field=models.UUIDField(default=uuid.UUID('bbe47c79-77fa-4348-81bf-bc42dcca60e2'), editable=False),
        ),
        migrations.AlterField(
            model_name='enquirie',
            name='Email',
            field=models.CharField(max_length=200),
        ),
    ]
