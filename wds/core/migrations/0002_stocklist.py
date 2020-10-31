# Generated by Django 3.1.1 on 2020-10-31 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StockList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stockname', models.CharField(max_length=100)),
                ('stockprice', models.IntegerField(default=0)),
            ],
        ),
    ]
