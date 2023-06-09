# Generated by Django 4.1.8 on 2023-06-06 01:24

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerceApp', '0011_alter_cheap_home_datepub_alter_cheap_home_unique_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cheap_home',
            name='DatePub',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 6, 2, 24, 56, 692912), editable=False, verbose_name='Date Created'),
        ),
        migrations.AlterField(
            model_name='cheap_home',
            name='unique_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name='cheaphomeimage',
            name='Created',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 6, 2, 24, 56, 693912)),
        ),
        migrations.AlterField(
            model_name='dream_mansion',
            name='DatePub',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 6, 2, 24, 56, 692912), editable=False, verbose_name='Date Created'),
        ),
        migrations.AlterField(
            model_name='dreammansionimage',
            name='Created',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 6, 2, 24, 56, 693912)),
        ),
        migrations.AlterField(
            model_name='emails',
            name='DatePub',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 6, 2, 24, 56, 691913), verbose_name='Date Created'),
        ),
    ]
