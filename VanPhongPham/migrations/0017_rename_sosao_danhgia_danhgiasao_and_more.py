# Generated by Django 5.0.4 on 2024-05-15 05:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("VanPhongPham", "0016_danhgia"),
    ]

    operations = [
        migrations.RenameField(
            model_name="danhgia",
            old_name="SoSao",
            new_name="DanhGiaSao",
        ),
        migrations.RemoveField(
            model_name="danhgia",
            name="DonHang",
        ),
        migrations.AddField(
            model_name="danhgia",
            name="san_pham",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="VanPhongPham.sanpham",
            ),
        ),
    ]
