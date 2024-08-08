# Generated by Django 5.0.7 on 2024-07-11 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='pic')),
                ('name', models.CharField(max_length=50)),
                ('desc', models.CharField(max_length=50)),
            ],
        ),
    ]
