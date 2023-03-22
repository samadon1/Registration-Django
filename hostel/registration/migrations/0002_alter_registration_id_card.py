# Generated by Django 4.1.7 on 2023-03-20 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='id_card',
            field=models.CharField(choices=[('G', 'Ghana Card'), ('N', 'National Health_Insurance Card'), ('V', "Voter's ID Card"), ('S', "Student's ID"), ('D', "Driver's License")], default='G', max_length=2),
        ),
    ]
