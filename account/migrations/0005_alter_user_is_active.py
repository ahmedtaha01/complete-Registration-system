# Generated by Django 4.1.1 on 2022-09-17 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_user_birthday_user_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(null=True),
        ),
    ]
