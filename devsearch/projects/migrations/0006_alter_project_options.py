# Generated by Django 5.0.3 on 2024-04-02 06:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_alter_project_options_review_owner_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-vote_ratio', '-vote_total', 'title']},
        ),
    ]
