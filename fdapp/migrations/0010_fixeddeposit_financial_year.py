# Generated by Django 5.1.6 on 2025-06-23 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fdapp', '0009_alter_fixeddeposit_bank_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='fixeddeposit',
            name='financial_year',
            field=models.CharField(blank=True, default='2024-25', max_length=10, null=True),
        ),
    ]
