# Generated by Django 3.2.3 on 2021-05-28 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0003_auto_20210528_1624'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='virtualartworkform',
            name='date_of_authorship',
        ),
        migrations.AddField(
            model_name='virtualartworkform',
            name='day',
            field=models.CharField(blank=True, default='', max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='virtualartworkform',
            name='month',
            field=models.CharField(blank=True, default='', max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='virtualartworkform',
            name='year',
            field=models.CharField(blank=True, default='', max_length=2, null=True),
        ),
    ]
