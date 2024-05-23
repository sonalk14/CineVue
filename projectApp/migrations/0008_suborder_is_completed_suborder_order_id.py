# Generated by Django 5.0.4 on 2024-05-11 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectApp', '0007_remove_subscriptions_user_suborder'),
    ]

    operations = [
        migrations.AddField(
            model_name='suborder',
            name='is_completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='suborder',
            name='order_id',
            field=models.CharField(default='0', max_length=50),
        ),
    ]