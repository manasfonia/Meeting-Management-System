# Generated by Django 3.0.1 on 2020-01-06 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0021_visitorinfo_checkout'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitorinfo',
            name='end_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='visitorinfo',
            name='start_time',
            field=models.DateTimeField(null=True),
        ),
    ]