# Generated by Django 4.0.4 on 2022-05-28 12:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_user_phone_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='images',
            old_name='post_date',
            new_name='pub_date',
        ),
    ]
