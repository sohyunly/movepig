# Generated by Django 3.1.7 on 2021-03-29 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0012_auto_20210329_1356'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_hit',
            field=models.PositiveIntegerField(default=0),
        ),
    ]