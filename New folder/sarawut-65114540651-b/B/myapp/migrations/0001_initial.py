# Generated by Django 5.1.3 on 2024-12-04 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='coruse',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.IntegerField(max_length=100)),
                ('info', models.IntegerField(max_length=100)),
            ],
        ),
    ]
