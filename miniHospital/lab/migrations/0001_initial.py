# Generated by Django 4.1 on 2022-09-11 13:51

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('doctor', '0003_alter_doctor_des_name_alter_doctor_email_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lab',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('year_of_service', models.DateField(default=datetime.date(2022, 9, 11))),
                ('qual_name', multiselectfield.db.fields.MultiSelectField(choices=[('DMLT', 'DMLT'), ('ADMLT', 'ADMLT'), ('BMLT', 'BMLT'), ('MLT', 'MLT')], max_length=100)),
                ('license_no', models.CharField(blank=True, max_length=100)),
                ('is_doctor', models.BooleanField(default=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_lab', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('des_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='des_name_lab', to='doctor.designation')),
                ('email', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('spec_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='spec_name_realted', to='doctor.specialization')),
            ],
        ),
    ]