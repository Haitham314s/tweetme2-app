# Generated by Django 4.2.2 on 2023-06-11 09:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tweets',
            new_name='Tweet',
        ),
    ]