# Generated by Django 4.2 on 2023-04-18 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AboutUs",
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
                ("first_name", models.CharField(max_length=255, null=True)),
                ("last_name", models.CharField(max_length=255, null=True)),
                ("role", models.CharField(max_length=255, null=True)),
                ("description", models.TextField()),
                (
                    "image",
                    models.ImageField(default="default.jpg", upload_to="about_us_pics"),
                ),
                ("created", models.DateField(auto_now_add=True)),
                ("updated", models.DateField(auto_now=True)),
            ],
        ),
    ]