# Generated by Django 3.0.3 on 2020-08-07 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PassengerDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('MA', 'Male'), ('FM', 'Female')], max_length=50)),
                ('coach', models.CharField(choices=[('S1', 'S1'), ('S2', 'S2'), ('S3', 'S3'), ('S4', 'S4')], max_length=50)),
                ('berth_preference', models.CharField(choices=[('UPR', 'Upper'), ('LWR', 'Lower'), ('MID', 'Middle'), ('SID', 'Side portion')], max_length=50)),
                ('ticket_type', models.CharField(choices=[('CF', 'Confirm'), ('RAC ', 'Reservation Against Cancellation'), ('WL', 'Waiting List')], max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
