# Generated by Django 3.0.3 on 2020-03-14 11:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EventCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EventVenue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('venure_name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EventRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host_name', models.CharField(max_length=50)),
                ('contact_number', models.IntegerField()),
                ('host_email_id', models.EmailField(max_length=100)),
                ('date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('budget', models.CharField(max_length=30)),
                ('special_requirements', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('event_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.EventCategory')),
                ('select_vanue_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='select_vanue_1', to='user.EventVenue')),
                ('select_vanue_2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='select_vanue_2', to='user.EventVenue')),
                ('select_vanue_3', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='select_vanue_3', to='user.EventVenue')),
            ],
        ),
    ]
