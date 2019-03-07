# Generated by Django 2.1.7 on 2019-03-07 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Flats', '0013_flatapplication'),
    ]

    operations = [
        migrations.CreateModel(
            name='FlatImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='flat_images/')),
                ('flat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Flats.FlatDetails')),
            ],
        ),
    ]
