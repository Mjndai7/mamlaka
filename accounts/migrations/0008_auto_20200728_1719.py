# Generated by Django 3.0.8 on 2020-07-28 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20200728_1701'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employeeprofile',
            old_name='Department',
            new_name='department',
        ),
        migrations.RenameField(
            model_name='employeeprofile',
            old_name='Job_title',
            new_name='job_title',
        ),
        migrations.RemoveField(
            model_name='employeeprofile',
            name='updated_on',
        ),
    ]
