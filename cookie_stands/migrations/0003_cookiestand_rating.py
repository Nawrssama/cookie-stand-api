# Generated by Django 4.1.5 on 2023-07-16 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookie_stands', '0002_remove_cookiestand_rating_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cookiestand',
            name='rating',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
