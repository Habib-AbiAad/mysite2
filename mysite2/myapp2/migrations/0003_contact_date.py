# Generated by Django 3.2.21 on 2023-10-03 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp2', '0002_auto_20231002_1405'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='date',
            field=models.DateField(default=985),
        ),
    ]
