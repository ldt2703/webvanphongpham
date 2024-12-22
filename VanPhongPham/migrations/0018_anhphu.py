# Generated by Django 5.0.4 on 2024-05-15 06:03

import VanPhongPham.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("VanPhongPham", "0017_rename_sosao_danhgia_danhgiasao_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="AnhPhu",
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
                (
                    "Anh",
                    models.ImageField(upload_to=VanPhongPham.models.upload_to_image),
                ),
                (
                    "san_pham",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="VanPhongPham.sanpham",
                    ),
                ),
            ],
        ),
    ]