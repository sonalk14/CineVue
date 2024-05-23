# Generated by Django 5.0.4 on 2024-05-08 16:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectApp', '0003_wishlist_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlist',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='projectApp.movie'),
        ),
    ]
