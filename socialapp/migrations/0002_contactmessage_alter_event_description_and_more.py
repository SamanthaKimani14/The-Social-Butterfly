# Generated by Django 5.0.3 on 2024-12-05 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('send_copy', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_type',
            field=models.CharField(choices=[('corporate', 'Corporate'), ('peer', 'Peer'), ('entertainment', 'Entertainment'), ('teen', 'Teen'), ('children', 'Children')], max_length=50),
        ),
    ]
