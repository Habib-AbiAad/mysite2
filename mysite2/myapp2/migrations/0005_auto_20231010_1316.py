# Generated by Django 3.2.21 on 2023-10-10 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp2', '0004_remove_contact_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='pass1',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='pass2',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
