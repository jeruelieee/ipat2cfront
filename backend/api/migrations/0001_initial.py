# Generated by Django 5.0.4 on 2024-07-08 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('permanent_address', models.TextField()),
                ('zip_code', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=20)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('place_of_birth', models.CharField(blank=True, max_length=100, null=True)),
                ('civil_status', models.CharField(blank=True, max_length=20, null=True)),
                ('sex', models.CharField(blank=True, max_length=10, null=True)),
                ('height', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('weight', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('bloodtype', models.CharField(blank=True, max_length=10, null=True)),
                ('citizenship', models.CharField(blank=True, max_length=50, null=True)),
                ('gsis', models.CharField(blank=True, max_length=20, null=True)),
                ('pag_ibig_no', models.CharField(blank=True, max_length=20, null=True)),
                ('philhealth', models.CharField(blank=True, max_length=20, null=True)),
                ('sss', models.CharField(blank=True, max_length=20, null=True)),
                ('tin', models.CharField(blank=True, max_length=20, null=True)),
                ('agency_employee_no', models.CharField(blank=True, max_length=100, null=True)),
                ('occupation', models.CharField(blank=True, max_length=100, null=True)),
                ('employee_business', models.CharField(blank=True, max_length=100, null=True)),
                ('business_address', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
