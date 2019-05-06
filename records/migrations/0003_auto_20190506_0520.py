# Generated by Django 2.2.1 on 2019-05-06 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0002_remove_customusers_countrycode'),
    ]

    operations = [
        migrations.AddField(
            model_name='customusers',
            name='countrycode',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='customusers',
            name='contactnumber',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='customusers',
            name='pincode',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
