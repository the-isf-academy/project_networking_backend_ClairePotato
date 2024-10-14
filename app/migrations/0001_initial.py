# Generated by Django 5.1.2 on 2024-10-14 03:41

import banjo.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Biology',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('views', banjo.models.IntegerField(default=0)),
                ('concept', banjo.models.StringField(default='')),
                ('related_keywords', banjo.models.StringField(default='')),
                ('archive', banjo.models.BooleanField(default=False)),
                ('confused', banjo.models.BooleanField(default=False)),
                ('confused_percentage', banjo.models.FloatField(default=0.0)),
                ('discussion', banjo.models.StringField(default='')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
