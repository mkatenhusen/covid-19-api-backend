# Generated by Django 3.0.4 on 2020-03-22 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('county', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='county',
            name='ags',
            field=models.CharField(help_text='Amtlicher Gemeindeschlüssel', max_length=10, unique=True),
        ),
    ]
