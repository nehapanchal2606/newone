# Generated by Django 4.0.2 on 2022-02-24 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='dep_code',
            field=models.IntegerField(default=-1),
            preserve_default=False,
        ),
    ]