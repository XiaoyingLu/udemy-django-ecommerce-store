# Generated by Django 5.0.1 on 2024-03-06 00:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="ShippingAddress",
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
                ("full_name", models.CharField(max_length=300)),
                ("email", models.EmailField(max_length=255)),
                ("address1", models.CharField(max_length=300)),
                ("address2", models.CharField(max_length=300)),
                ("city", models.CharField(blank=True, max_length=255, null=True)),
                ("state", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Shipping Address",
            },
        ),
    ]
