# Generated by Django 3.2.1 on 2021-07-05 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bankapp', '0008_alter_transaction_tdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='tdate',
            field=models.DateTimeField(),
        ),
    ]
