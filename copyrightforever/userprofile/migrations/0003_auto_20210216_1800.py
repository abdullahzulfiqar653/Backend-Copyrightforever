# Generated by Django 3.1.6 on 2021-02-16 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0002_awein_natureofauthorship'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Awein',
        ),
        migrations.DeleteModel(
            name='NatureOfAuthorship',
        ),
    ]
