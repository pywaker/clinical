# Generated by Django 2.0.1 on 2018-01-08 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0011_clinicemployee_labemployee_pharmacyemployee'),
    ]

    operations = [
        migrations.AddField(
            model_name='labtickets',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
