# Generated by Django 4.2.7 on 2023-11-10 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='questionchoice',
            old_name='Choice',
            new_name='choice',
        ),
        migrations.AlterField(
            model_name='questionresponse',
            name='first_name',
            field=models.CharField(blank=True, default='Default', max_length=100),
        ),
        migrations.AlterUniqueTogether(
            name='questionchoice',
            unique_together={('question', 'position'), ('question', 'choice')},
        ),
    ]
