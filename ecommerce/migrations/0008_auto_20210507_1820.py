# Generated by Django 3.1.5 on 2021-05-07 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0007_auto_20210505_1609'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='description',
        ),
        migrations.AddField(
            model_name='product',
            name='d1',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='d2',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='d3',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='d4',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='d5',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='d6',
            field=models.CharField(max_length=80, null=True),
        ),
    ]
