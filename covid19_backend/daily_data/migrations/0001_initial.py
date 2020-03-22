# Generated by Django 3.0.4 on 2020-03-22 11:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('county', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Age',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('min', models.SmallIntegerField()),
                ('max', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=6, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='DailyCase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('infected_total', models.IntegerField()),
                ('deaths_total', models.IntegerField()),
                ('healed_total', models.IntegerField(blank=True, null=True)),
                ('immune_total', models.IntegerField(blank=True, null=True)),
                ('intensive_total', models.IntegerField(blank=True, null=True)),
                ('date_day', models.DateField()),
                ('last_updated', models.DateTimeField()),
                ('county', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='county.County')),
            ],
        ),
        migrations.CreateModel(
            name='GenderAgeRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_day', models.DateField()),
                ('count', models.IntegerField()),
                ('last_updated', models.DateTimeField()),
                ('age', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='daily_data.Age')),
                ('county', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='county.County')),
                ('gender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='daily_data.Gender')),
            ],
            options={
                'unique_together': {('county', 'date_day', 'age', 'gender')},
            },
        ),
    ]
