# Generated by Django 4.2.7 on 2023-11-10 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0005_alter_questionresponse_status_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionresponse',
            name='data_science_class_1',
            field=models.CharField(default='Default', max_length=100),
        ),
        migrations.AddField(
            model_name='questionresponse',
            name='data_science_class_2',
            field=models.CharField(default='Default', max_length=100),
        ),
        migrations.AddField(
            model_name='questionresponse',
            name='data_science_class_3',
            field=models.CharField(default='Default', max_length=100),
        ),
        migrations.AddField(
            model_name='questionresponse',
            name='department',
            field=models.CharField(default='Default', max_length=100),
        ),
        migrations.AddField(
            model_name='questionresponse',
            name='google_scholar',
            field=models.CharField(default='Default', max_length=100),
        ),
        migrations.AddField(
            model_name='questionresponse',
            name='research_description',
            field=models.CharField(default='Default', max_length=150),
        ),
        migrations.AddField(
            model_name='questionresponse',
            name='research_example',
            field=models.TextField(default='Default', max_length=500),
        ),
        migrations.AddField(
            model_name='questionresponse',
            name='research_tagline',
            field=models.CharField(default='Default', max_length=300),
        ),
        migrations.AddField(
            model_name='questionresponse',
            name='reserach_count',
            field=models.CharField(default='Default', max_length=100),
        ),
        migrations.AddField(
            model_name='questionresponse',
            name='semantic_scholar',
            field=models.CharField(default='Default', max_length=100),
        ),
        migrations.AddField(
            model_name='questionresponse',
            name='university',
            field=models.CharField(default='Default', max_length=100),
        ),
        migrations.AddField(
            model_name='questionresponse',
            name='university_desc',
            field=models.TextField(default='Default', max_length=500),
        ),
        migrations.AddField(
            model_name='questionresponse',
            name='university_link',
            field=models.CharField(default='Default', max_length=100),
        ),
        migrations.AddField(
            model_name='questionresponse',
            name='university_title',
            field=models.CharField(default='Default', max_length=100),
        ),
    ]