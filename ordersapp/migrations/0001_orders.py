# Generated by Django 3.2.12 on 2022-02-07 19:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("mainapp", "0006_product_is_active"),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created", models.DateTimeField(auto_now_add=True, verbose_name="создан")),
                ("updated", models.DateTimeField(auto_now=True, verbose_name="обновлен")),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("FM", "формируется"),
                            ("STP", "отправлен в обработку"),
                            ("PD", "оплачен"),
                            ("PRD", "обрабатывается"),
                            ("RDY", "готов к выдаче"),
                            ("CNC", "отменен"),
                        ],
                        default="FM",
                        max_length=3,
                        verbose_name="статус",
                    ),
                ),
                ("is_active", models.BooleanField(default=True, verbose_name="активен")),
                ("user", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                "verbose_name": "заказ",
                "verbose_name_plural": "заказы",
                "ordering": ("-created",),
            },
        ),
        migrations.CreateModel(
            name="OrderItem",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("quantity", models.PositiveIntegerField(default=0, verbose_name="количество")),
                (
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="orderitems", to="ordersapp.order"
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="mainapp.product", verbose_name="продукт"
                    ),
                ),
            ],
        ),
    ]
