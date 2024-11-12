# Generated by Django 3.2.5 on 2024-11-12 04:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('geography', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusStop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bus_stops', to='geography.place')),
            ],
        ),
    ]