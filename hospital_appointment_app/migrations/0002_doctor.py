# Generated by Django 3.2.4 on 2021-06-19 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_appointment_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=250)),
                ('mobile', models.CharField(max_length=10)),
                ('department', models.CharField(choices=[('Cardiologists', 'Cardiology'), ('Dermatology', 'Dermatology'), ('Immunology', 'Immunology'), ('Anesthesiology', 'Anesthesiology'), ('Emergency', 'Emergency')], default='Cardiologist', max_length=50)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
    ]
