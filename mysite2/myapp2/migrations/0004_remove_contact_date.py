# Generated by Django 3.2.21 on 2023-10-08 07:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp2', '0003_contact_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='date',
        ),
    ]
