# Generated by Django 5.1.6 on 2025-03-08 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='published_date',
            field=models.DateField(default='2000-01-01'),
        ),
    ]
