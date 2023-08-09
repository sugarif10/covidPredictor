# Generated by Django 3.2.6 on 2021-08-11 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CovidList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BreathingProblem', models.CharField(max_length=5)),
                ('Fever', models.CharField(max_length=5)),
                ('DryCough', models.CharField(max_length=5)),
                ('Sorethroat', models.CharField(max_length=5)),
                ('RunningNose', models.CharField(max_length=5)),
                ('Asthma', models.CharField(max_length=5)),
                ('Headache', models.CharField(max_length=5)),
                ('HeartDisease', models.CharField(max_length=5)),
                ('Diabetes', models.CharField(max_length=5)),
                ('Hypertension', models.CharField(max_length=5)),
                ('Fatigue', models.CharField(max_length=5)),
                ('AbroadTravel', models.CharField(max_length=5)),
                ('ContactCovidPatient', models.CharField(max_length=5)),
                ('AttendedLargeGathering', models.CharField(max_length=5)),
                ('VisitedPublic', models.CharField(max_length=5)),
                ('FamilyWorkingPublic', models.CharField(max_length=5)),
            ],
        ),
    ]
