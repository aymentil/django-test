# Generated by Django 3.2.5 on 2024-11-12 04:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('geography', '0002_busstop'),
        ('fleet', '0002_auto_20211109_1456'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusShift',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField(verbose_name='Start of the shift')),
                ('end', models.DateTimeField(verbose_name='End of the shift')),
                ('bus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shifts', to='fleet.bus')),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shifts', to='fleet.driver')),
            ],
            options={
                'ordering': ['start'],
            },
        ),
        migrations.CreateModel(
            name='BusShiftStop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(verbose_name='Order of the stop')),
                ('bus_shift', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fleet.busshift')),
                ('bus_stop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='geography.busstop')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.AddField(
            model_name='busshift',
            name='stops',
            field=models.ManyToManyField(related_name='shifts', through='fleet.BusShiftStop', to='geography.BusStop'),
        ),
    ]
