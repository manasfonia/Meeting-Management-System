# Generated by Django 3.0.1 on 2019-12-27 11:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0012_auto_20191227_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitorinfo',
            name='host',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firstapp.EmployeeInfo'),
        ),
    ]
