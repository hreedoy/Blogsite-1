# Generated by Django 3.2 on 2021-04-18 06:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_post_cat_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='cat_count',
        ),
    ]
