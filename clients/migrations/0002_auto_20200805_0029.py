# Generated by Django 3.0.8 on 2020-08-04 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaser',
            name='email',
            field=models.EmailField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='purchaser',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
