# Generated by Django 4.0 on 2024-05-16 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('importfiles', '0005_remove_initialuploadedfile_date_processed_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='initialuploadedfile',
            name='decimal_separator',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='initialuploadedfile',
            name='thousand_separator',
            field=models.CharField(default='', max_length=10),
        ),
    ]
