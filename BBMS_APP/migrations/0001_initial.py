# Generated by Django 4.2.10 on 2024-04-23 18:12

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BloodBankRecord',
            fields=[
                ('blood_bank_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('blood_bank_name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('mobile', models.CharField(max_length=13)),
                ('email', models.EmailField(max_length=50)),
            ],
            options={
                'db_table': 'BLOODBANK_RECORD',
            },
        ),
        migrations.CreateModel(
            name='BloodGroupRecord',
            fields=[
                ('blood_group_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('blood_group_name', models.CharField(max_length=11)),
                ('donated_blood_to', models.CharField(max_length=255)),
                ('received_blood_from', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'BLOOD_GROUP',
            },
        ),
        migrations.CreateModel(
            name='CustomerDetails',
            fields=[
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('phone', models.CharField(max_length=10, unique=True)),
                ('gender', models.CharField(max_length=6)),
                ('blood_group', models.CharField(max_length=3)),
                ('profile_photo', models.ImageField(blank=True, null=True, upload_to='user_profile_photos/')),
                ('user_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=15)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'CUSTOMER_DETAILS',
            },
        ),
        migrations.CreateModel(
            name='DoctorDetails',
            fields=[
                ('doctor_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=6)),
                ('specialization', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.CharField(max_length=13)),
                ('address', models.CharField(max_length=100)),
                ('profile_photo', models.ImageField(blank=True, null=True, upload_to='user_profile_photos/')),
            ],
            options={
                'db_table': 'DOCTOR_DETAILS',
            },
        ),
        migrations.CreateModel(
            name='DonorDetails',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=13)),
                ('email', models.EmailField(max_length=15)),
                ('gender', models.CharField(max_length=10)),
                ('blood_group', models.CharField(max_length=4)),
                ('district', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=500)),
                ('profile_photo', models.ImageField(blank=True, null=True, upload_to='donor_profile_photos/')),
                ('donor_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=15)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, null=True)),
            ],
            options={
                'db_table': 'DONOR_DETAILS',
            },
        ),
        migrations.CreateModel(
            name='MainBloodBankSystem',
            fields=[
                ('district_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('district_name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'db_table': 'MAIN_BLOODBANK_SYSTEM',
            },
        ),
        migrations.CreateModel(
            name='DonorLoginSession',
            fields=[
                ('session_number', models.AutoField(primary_key=True, serialize=False)),
                ('login_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('logout_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BBMS_APP.donordetails')),
            ],
            options={
                'db_table': 'DONOR_LOGIN&LOGOUT',
            },
        ),
        migrations.CreateModel(
            name='CustomerOrderDetails',
            fields=[
                ('order_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('order_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.CharField(max_length=13)),
                ('blood_group', models.CharField(default='', max_length=13)),
                ('packets', models.IntegerField(default=0)),
                ('amount', models.IntegerField(default=0)),
                ('district', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=100)),
                ('additional', models.CharField(max_length=1000)),
                ('customer_id', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='BBMS_APP.customerdetails')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerLoginSession',
            fields=[
                ('session_id', models.CharField(default='', max_length=20, primary_key=True, serialize=False)),
                ('login_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('logout_time', models.DateTimeField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BBMS_APP.customerdetails')),
            ],
            options={
                'db_table': 'CUSTOMER_LOGIN&LOGOUT',
            },
        ),
        migrations.CreateModel(
            name='BloodDonation',
            fields=[
                ('donation_id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.CharField(max_length=7)),
                ('district', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=100)),
                ('donation_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('doctor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BBMS_APP.doctordetails')),
                ('donor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BBMS_APP.donordetails')),
            ],
            options={
                'db_table': 'BLOOD_DONATION_RECORDS',
            },
        ),
        migrations.CreateModel(
            name='BloodBankStockRecord',
            fields=[
                ('record_id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField(default=0)),
                ('blood_bank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BBMS_APP.bloodbankrecord')),
                ('blood_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BBMS_APP.bloodgrouprecord')),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BBMS_APP.mainbloodbanksystem')),
            ],
            options={
                'db_table': 'BLOOD_BANK',
            },
        ),
        migrations.AddField(
            model_name='bloodbankrecord',
            name='district',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BBMS_APP.mainbloodbanksystem'),
        ),
    ]
