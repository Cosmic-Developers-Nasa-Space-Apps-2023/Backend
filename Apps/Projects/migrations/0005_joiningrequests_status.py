# Generated by Django 4.1.10 on 2023-10-07 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Projects", "0004_alter_project_field_alter_project_status_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="joiningrequests",
            name="status",
            field=models.CharField(
                choices=[("P", "Pending"), ("A", "Accepted"), ("R", "Rejected")],
                default="P",
                max_length=100,
                null=True,
                verbose_name="status",
            ),
        ),
    ]