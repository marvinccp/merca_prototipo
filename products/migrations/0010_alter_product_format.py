# Generated by Django 4.1.3 on 2022-12-22 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_product_format_alter_product_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='format',
            field=models.CharField(default='1Kg', max_length=50),
        ),
    ]