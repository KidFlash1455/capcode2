# Generated by Django 4.2.7 on 2023-11-10 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0004_questionresponse_status_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionresponse',
            name='status_desc',
            field=models.TextField(default='Default', max_length=500),
        ),
    ]
