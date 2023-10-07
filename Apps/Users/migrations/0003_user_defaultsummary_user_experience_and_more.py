# Generated by Django 4.1.10 on 2023-10-07 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Users", "0002_profile"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="defaultSummary",
            field=models.TextField(
                blank=True, max_length=500, null=True, verbose_name="DefaultSummary"
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="experience",
            field=models.JSONField(blank=True, null=True, verbose_name="Esperience"),
        ),
        migrations.AddField(
            model_name="user",
            name="seeking_fields",
            field=models.JSONField(blank=True, null=True, verbose_name="SeekingSkills"),
        ),
        migrations.AddField(
            model_name="user",
            name="skills",
            field=models.JSONField(blank=True, null=True, verbose_name="skills"),
        ),
        migrations.AddField(
            model_name="user",
            name="working_availability",
            field=models.DateField(null=True),
        ),
    ]