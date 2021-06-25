# Generated by Django 3.1.6 on 2021-06-25 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LoanApp', '0004_auto_20210625_1121'),
    ]

    operations = [
        migrations.RenameField(
            model_name='amountloan',
            old_name='Payment',
            new_name='TotalInterest',
        ),
        migrations.AddField(
            model_name='amountloan',
            name='MonthlyPayment',
            field=models.CharField(default='', max_length=100000),
        ),
        migrations.AddField(
            model_name='amountloan',
            name='TotalPayment',
            field=models.CharField(default='', max_length=1000000),
        ),
    ]