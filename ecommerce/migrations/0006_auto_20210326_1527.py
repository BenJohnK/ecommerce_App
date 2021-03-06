# Generated by Django 3.1.5 on 2021-03-26 09:57

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0005_auto_20210321_1552'),
    ]

    operations = [
        migrations.AddField(
            model_name='shippingdetails',
            name='address',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='shippingdetails',
            name='city',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='shippingdetails',
            name='country',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='shippingdetails',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ecommerce.customer'),
        ),
        migrations.AddField(
            model_name='shippingdetails',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shippingdetails',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ecommerce.order'),
        ),
        migrations.AddField(
            model_name='shippingdetails',
            name='state',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
