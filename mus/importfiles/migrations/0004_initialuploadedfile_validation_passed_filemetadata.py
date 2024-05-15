# Generated by Django 4.0 on 2024-05-15 18:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('importfiles', '0003_initialuploadedfile_txt_column_delimiter'),
    ]

    operations = [
        migrations.AddField(
            model_name='initialuploadedfile',
            name='validation_passed',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='FileMetaData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sum', models.FloatField()),
                ('elements_number', models.IntegerField()),
                ('file', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='importfiles.initialuploadedfile')),
            ],
        ),
    ]