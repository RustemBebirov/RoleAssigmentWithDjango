# Generated by Django 3.2.6 on 2021-08-07 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='create',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='delete',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='read',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='update',
            field=models.BooleanField(default=True),
        ),
    ]
