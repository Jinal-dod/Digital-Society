# Generated by Django 3.1.7 on 2021-04-03 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chairman', '0011_watchman_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchman',
            name='address',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='watchman',
            name='age',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='watchman',
            name='blood_group',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='watchman',
            name='email',
            field=models.EmailField(max_length=35),
        ),
        migrations.AlterField(
            model_name='watchman',
            name='family_contact',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]