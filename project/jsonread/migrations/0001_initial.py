# Generated by Django 3.1.1 on 2020-09-07 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataRead',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dr_id', models.IntegerField()),
                ('dr_fname', models.CharField(max_length=15)),
                ('dr_lname', models.CharField(max_length=15)),
            ],
        ),
    ]
