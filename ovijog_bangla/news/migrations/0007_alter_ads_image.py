# Generated by Django 3.2.6 on 2022-04-18 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_ads'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ads',
            name='image',
            field=models.FileField(upload_to='ads_img'),
        ),
    ]
