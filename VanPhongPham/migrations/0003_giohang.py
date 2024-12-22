# Generated by Django 5.0.4 on 2024-05-11 01:01

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("VanPhongPham", "0002_remove_sanpham_masp"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="GioHang",
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
                ("so_luong", models.CharField(default="1", max_length=100)),
                ("ngay_tao", models.DateTimeField(auto_now_add=True)),
                (
                    "san_pham",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="VanPhongPham.sanpham",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]