# Generated by Django 3.2.5 on 2021-07-20 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='investmnet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('investor', models.CharField(max_length=100)),
                ('Borrower', models.CharField(max_length=100)),
                ('amount', models.IntegerField()),
                ('date', models.DateTimeField()),
            ],
        ),
    ]