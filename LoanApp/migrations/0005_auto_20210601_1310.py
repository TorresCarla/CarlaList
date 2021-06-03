# Generated by Django 3.1.6 on 2021-06-01 13:10

import LoanApp.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('LoanApp', '0004_auto_20210501_1431'),
    ]

    operations = [
        migrations.CreateModel(
            name='LogIn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FullName', models.TextField(default='', verbose_name=LoanApp.models.Loaner)),
                ('EmailAddress', models.TextField(default='', verbose_name=LoanApp.models.Loaner)),
                ('Password', models.TextField(default='', verbose_name=LoanApp.models.Loaner)),
            ],
        ),
        migrations.RenameField(
            model_name='item',
            old_name='text',
            new_name='BankBranch',
        ),
        migrations.AddField(
            model_name='item',
            name='CompanyBranch',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='loaner',
            name='CellNo',
            field=models.CharField(default='', max_length=12),
        ),
        migrations.AddField(
            model_name='loaner',
            name='Citizenship',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='loaner',
            name='DateOfBirth',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='loaner',
            name='EmailAddress',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='loaner',
            name='Employment',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='loaner',
            name='Friend',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='loaner',
            name='FriendCellNo',
            field=models.CharField(default='', max_length=12),
        ),
        migrations.AddField(
            model_name='loaner',
            name='FullName',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='loaner',
            name='Income',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='loaner',
            name='ResidenceAddress',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='loaner',
            name='Status',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='loaner',
            name='ValidID',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='loaner',
            name='ValidIDNo',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AddField(
            model_name='loaner',
            name='ZipCode',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='item',
            name='LoanId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LoanApp.loaner'),
        ),
        migrations.CreateModel(
            name='Repayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PaymentMethod', models.TextField(default='')),
                ('GuidelinePayment', models.TextField(default='')),
                ('PayNow', models.TextField(default='')),
                ('LoanId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LoanApp.loaner')),
            ],
        ),
        migrations.CreateModel(
            name='AmountLoan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AmountLoan', models.CharField(default='', max_length=1000000)),
                ('Interest', models.CharField(default='', max_length=100)),
                ('Months', models.CharField(default='', max_length=72)),
                ('integer', models.IntegerField(default='', null=True)),
                ('LoanId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='LoanApp.loaner')),
            ],
        ),
    ]
