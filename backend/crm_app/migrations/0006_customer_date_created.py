# Generated by Django 4.1.3 on 2023-10-17 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm_app', '0005_remove_customer_date_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='date_created',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
