# Generated by Django 4.1.10 on 2023-10-07 22:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("Projects", "0005_joiningrequests_status"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="usersprojects",
            name="scope",
        ),
    ]