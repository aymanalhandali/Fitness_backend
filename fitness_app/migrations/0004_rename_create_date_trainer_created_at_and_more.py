# Generated by Django 4.2.4 on 2023-09-13 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitness_app', '0003_alter_trainer_create_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trainer',
            old_name='create_date',
            new_name='created_at',
        ),
        migrations.AddField(
            model_name='trainer',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
