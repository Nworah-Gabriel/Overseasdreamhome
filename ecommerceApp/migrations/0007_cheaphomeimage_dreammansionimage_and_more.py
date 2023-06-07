# Generated by Django 4.1.8 on 2023-06-03 18:37

import datetime
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerceApp', '0006_cheap_home_description_dream_mansion_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CheapHomeImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Created', models.DateTimeField(default=datetime.datetime(2023, 6, 3, 19, 37, 40, 262648))),
                ('ImageUrl', models.CharField(max_length=2000)),
                ('unique_id', models.UUIDField(default=uuid.uuid4, editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='DreamMansionImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Created', models.DateTimeField(default=datetime.datetime(2023, 6, 3, 19, 37, 40, 261648))),
                ('ImageUrl', models.CharField(max_length=2000)),
                ('unique_id', models.UUIDField(default=uuid.uuid4, editable=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='dreammansionimages',
            name='DreamMansion',
        ),
        migrations.AlterField(
            model_name='cheap_home',
            name='DatePub',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 3, 19, 37, 40, 260648), editable=False, verbose_name='Date Created'),
        ),
        migrations.AlterField(
            model_name='cheap_home',
            name='Description',
            field=models.TextField(default='Write an organized description of the asset to be displayed.'),
        ),
        migrations.AlterField(
            model_name='cheap_home',
            name='unique_id',
            field=models.UUIDField(default=uuid.UUID('358782aa-efa1-45e3-b368-4a06976cd5fc'), editable=False),
        ),
        migrations.AlterField(
            model_name='dream_mansion',
            name='DatePub',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 3, 19, 37, 40, 261648), editable=False, verbose_name='Date Created'),
        ),
        migrations.AlterField(
            model_name='dream_mansion',
            name='Description',
            field=models.TextField(default='Write an organized description of the asset to be displayed.'),
        ),
        migrations.AlterField(
            model_name='dream_mansion',
            name='unique_id',
            field=models.UUIDField(default=uuid.UUID('c7df0956-2519-4a89-a1a8-62b815941395'), editable=False),
        ),
        migrations.DeleteModel(
            name='CheapHomeImages',
        ),
        migrations.DeleteModel(
            name='DreamMansionImages',
        ),
        migrations.AddField(
            model_name='dreammansionimage',
            name='DreamMansion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerceApp.dream_mansion'),
        ),
        migrations.AddField(
            model_name='cheaphomeimage',
            name='CheapHomes',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerceApp.cheap_home'),
        ),
    ]
