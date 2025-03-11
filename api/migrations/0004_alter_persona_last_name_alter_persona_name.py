# Generated by Django 4.2.2 on 2025-03-11 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_persona_last_name_alter_persona_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='last_name',
            field=models.CharField(help_text='Enter a last name', max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='name',
            field=models.CharField(help_text='Enter a name', max_length=200, unique=True),
        ),
    ]
