# Generated by Django 4.1.3 on 2022-12-22 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_alter_product_format'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='notes',
            field=models.CharField(default='Sin novedad', max_length=300),
        ),
    ]