# Generated by Django 4.0 on 2024-05-17 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0003_alter_analysis_sampled_units_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analysis',
            name='sampled_units_count',
            field=models.IntegerField(default=0),
        ),
    ]
