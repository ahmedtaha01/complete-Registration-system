# Generated by Django 4.1.1 on 2022-09-17 22:39

import django.core.validators
from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_alter_user_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='url_link',
        ),
        migrations.AddField(
            model_name='user',
            name='facebook',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='birthday',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='country',
            field=django_countries.fields.CountryField(blank=True, default='EG', max_length=2),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=14, validators=[django.core.validators.RegexValidator(message='phone must be an egyptian phone number...', regex='^01[1|0|2|5][0-9]{8}$')]),
        ),
    ]
