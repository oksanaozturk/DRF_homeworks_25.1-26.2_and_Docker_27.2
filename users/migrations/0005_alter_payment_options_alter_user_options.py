# Generated by Django 5.0.4 on 2024-06-03 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_payment_link_payment_session_id_alter_payment_amount'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='payment',
            options={'verbose_name': 'Платеж', 'verbose_name_plural': 'Платежи'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
    ]
