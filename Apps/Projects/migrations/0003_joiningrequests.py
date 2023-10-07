# Generated by Django 4.1.10 on 2023-10-07 15:49

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("Projects", "0002_usersprojects"),
    ]

    operations = [
        migrations.CreateModel(
            name="JoiningRequests",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("working_date", models.DateField()),
                ("summary", models.TextField(max_length=500, verbose_name="summary")),
                (
                    "project_id",
                    models.ManyToManyField(
                        related_name="joining_requests", to="Projects.project"
                    ),
                ),
                (
                    "user_id",
                    models.ManyToManyField(
                        related_name="joining_requests", to=settings.AUTH_USER_MODEL
                    ),
                ),
            ],
        ),
    ]
