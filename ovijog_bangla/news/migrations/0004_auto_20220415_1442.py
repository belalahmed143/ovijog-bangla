# Generated by Django 3.2.6 on 2022-04-15 08:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20211024_1511'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['-id']},
        ),
        migrations.CreateModel(
            name='NewsLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district', models.CharField(max_length=150)),
                ('division', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='chaild', to='news.newslocation')),
            ],
        ),
        migrations.AddField(
            model_name='news',
            name='news_location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='news.newslocation'),
        ),
    ]