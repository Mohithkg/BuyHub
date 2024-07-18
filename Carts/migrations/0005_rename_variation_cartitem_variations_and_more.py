# Generated by Django 5.0.7 on 2024-07-15 11:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Carts', '0004_rename_variations_cartitem_variation'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='variation',
            new_name='variations',
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='cart',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Carts.cart'),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]