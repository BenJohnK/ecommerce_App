# Generated by Django 3.1.5 on 2021-05-08 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0008_auto_20210507_1820'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='largeimage',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='d5',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='d6',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]