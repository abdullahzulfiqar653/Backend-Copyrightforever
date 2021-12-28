# Generated by Django 3.2.3 on 2021-06-16 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0008_auto_20210530_1353'),
    ]

    operations = [
        migrations.RenameField(
            model_name='performingartform',
            old_name='date_of_authorship',
            new_name='city',
        ),
        migrations.AddField(
            model_name='performingartform',
            name='day',
            field=models.CharField(blank=True, default='', max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='performingartform',
            name='month',
            field=models.CharField(blank=True, default='', max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='performingartform',
            name='state',
            field=models.CharField(blank=True, default='', max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='performingartform',
            name='year',
            field=models.CharField(blank=True, default='', max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='performingartform',
            name='zipcode',
            field=models.CharField(blank=True, default='', max_length=120, null=True),
        ),
    ]
