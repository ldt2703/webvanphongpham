# Generated by Django 5.0.4 on 2024-05-14 02:39

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("VanPhongPham", "0012_alter_donhang_ngay_tao"),
    ]

    operations = [
        migrations.AlterField(
            model_name="donhang",
            name="ngay_tao",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
