# Generated by Django 5.0.4 on 2024-05-11 00:16

import VanPhongPham.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Loai",
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
                ("TenLoai", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="SanPham",
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
                ("MaSP", models.IntegerField()),
                ("TenSP", models.CharField(max_length=100)),
                ("MoTa", models.TextField()),
                ("DonGia", models.CharField(max_length=100)),
                ("GiamGia", models.IntegerField()),
                (
                    "HinhAnh",
                    models.ImageField(upload_to=VanPhongPham.models.upload_to_image),
                ),
                (
                    "ML",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="dsSP",
                        to="VanPhongPham.loai",
                    ),
                ),
            ],
        ),
    ]
