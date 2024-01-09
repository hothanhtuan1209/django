# Generated by Django 4.2.8 on 2024-01-09 07:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("contacts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="contact",
            name="archived",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="contact",
            name="modified_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
