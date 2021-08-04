# Generated by Django 3.2.3 on 2021-05-31 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0006_delete_phonemodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='contactus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.BigIntegerField()),
                ('message', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ordernow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('adress', models.CharField(max_length=200)),
            ],
        ),
    ]
