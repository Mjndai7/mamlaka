# Generated by Django 3.0.8 on 2020-07-28 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20200728_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeedetails',
            name='job_title',
            field=models.CharField(choices=[('CEO', 'CEO'), ('HEAD', 'HEAD'), ('MANAGER', 'MANAGER'), ('SENIOR', 'SENIOR'), ('ACCOUNTANT', 'ACCOUNTANT'), ('JUNIOR', 'JUNIOR'), ('GUARD', 'GUARD'), ('CONSULTANT', 'CONSULTANT')], max_length=50),
        ),
    ]