# Generated by Django 4.2.4 on 2023-09-15 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitness_app', '0004_rename_create_date_trainer_created_at_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trainer',
            old_name='created_at',
            new_name='date',
        ),
        migrations.RemoveField(
            model_name='trainer',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='session',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]
