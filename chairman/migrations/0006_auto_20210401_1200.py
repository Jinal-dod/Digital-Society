# Generated by Django 3.1.7 on 2021-04-01 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chairman', '0005_auto_20210319_1448'),
    ]

    operations = [
        migrations.CreateModel(
            name='complain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='events',
            name='event_pic',
            field=models.FileField(blank=True, default='default.jpg', upload_to='img/'),
        ),
    ]
