# Generated by Django 3.0.3 on 2020-05-01 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20200501_2348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='profile_pic',
            field=models.ImageField(blank=True, default='logo_4.PNG', null=True, upload_to=''),
        ),
    ]
