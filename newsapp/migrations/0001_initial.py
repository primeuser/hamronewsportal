# Generated by Django 2.1.4 on 2019-01-03 08:04

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('descritpion', models.TextField()),
                ('image', models.ImageField(upload_to='post_photo')),
                ('date_created', models.DateTimeField(blank=True, default=datetime.datetime(2019, 1, 3, 8, 4, 0, 769910, tzinfo=utc))),
                ('author', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PostCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='newsapp.PostCategory'),
        ),
    ]
