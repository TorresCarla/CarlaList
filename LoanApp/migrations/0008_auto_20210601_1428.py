# Generated by Django 3.1.6 on 2021-06-01 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LoanApp', '0007_auto_20210601_1426'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Amount',
            new_name='AmountLoan',
        ),
    ]
