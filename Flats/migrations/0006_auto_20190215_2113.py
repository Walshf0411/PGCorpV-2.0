# Generated by Django 2.1.7 on 2019-02-15 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Flats', '0005_remove_flatdetails_parking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flatdetails',
            name='datetime',
            field=models.DateTimeField(auto_now=True),
        ),
    ]