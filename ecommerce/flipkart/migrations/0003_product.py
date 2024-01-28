# Generated by Django 4.2.7 on 2024-01-17 06:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("flipkart", "0002_category"),
    ]

    operations = [
        migrations.CreateModel(
            name="product",
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
                ("product_image", models.ImageField(upload_to="upload/category/")),
                (
                    "product_name",
                    models.CharField(default="", max_length=100, null=True),
                ),
                ("product_price", models.IntegerField(default=1)),
                (
                    "product_desc",
                    models.CharField(default="", max_length=100, null=True),
                ),
                (
                    "product_caregory",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="flipkart.category",
                    ),
                ),
            ],
        ),
    ]
