# Generated by Django 5.0.7 on 2024-07-11 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0006_rename_cus_name_booking_customer_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='event_name',
            new_name='name',
        ),
    ]
