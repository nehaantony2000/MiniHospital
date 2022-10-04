# Generated by Django 4.1 on 2022-10-01 11:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_account_dob'),
    ]

    operations = [
        migrations.CreateModel(
            name='demo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('file_field', models.FileField(upload_to='documents/')),
            ],
        ),
        migrations.AlterField(
            model_name='account',
            name='dob',
            field=models.DateField(default=datetime.date(2022, 10, 1)),
        ),
        migrations.AlterField(
            model_name='account',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]