# Generated by Django 3.2.6 on 2022-04-15 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20220415_1442'),
    ]

    operations = [
        migrations.AddField(
            model_name='newslocation',
            name='division_status',
            field=models.BooleanField(default=False),
        ),
    ]
