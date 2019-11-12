# Generated by Django 2.2.7 on 2019-11-12 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User_Id', models.CharField(max_length=100)),
                ('First_Name', models.CharField(max_length=100)),
                ('Last_Name', models.CharField(max_length=100)),
                ('Email_Id', models.CharField(max_length=100)),
                ('Password', models.CharField(max_length=20)),
                ('AddressLine1', models.CharField(max_length=100)),
                ('AddressLine2', models.CharField(default='', max_length=100)),
                ('City', models.CharField(max_length=100)),
                ('Pincode', models.CharField(max_length=10)),
                ('contactNumber', models.IntegerField(max_length=15)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CustomerAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User_Id', models.CharField(max_length=100)),
                ('First_Name', models.CharField(max_length=100)),
                ('Last_Name', models.CharField(max_length=100)),
                ('Email_Id', models.CharField(max_length=100)),
                ('Password', models.CharField(max_length=20)),
                ('AddressLine1', models.CharField(max_length=100)),
                ('AddressLine2', models.CharField(default='', max_length=100)),
                ('City', models.CharField(max_length=100)),
                ('Pincode', models.CharField(max_length=10)),
                ('contactNumber', models.IntegerField(max_length=15)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DriverAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User_Id', models.CharField(max_length=100)),
                ('First_Name', models.CharField(max_length=100)),
                ('Last_Name', models.CharField(max_length=100)),
                ('Email_Id', models.CharField(max_length=100)),
                ('Password', models.CharField(max_length=20)),
                ('AddressLine1', models.CharField(max_length=100)),
                ('AddressLine2', models.CharField(default='', max_length=100)),
                ('City', models.CharField(max_length=100)),
                ('Pincode', models.CharField(max_length=10)),
                ('contactNumber', models.IntegerField(max_length=15)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]