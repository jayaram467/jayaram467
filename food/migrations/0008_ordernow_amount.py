# Generated by Django 3.2.3 on 2021-06-26 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0007_contactus_ordernow'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordernow',
            name='amount',
            field=models.CharField(choices=[('MEALS', (('120', '120'),)), ('CHICKEN BIRAYANI', (('180', '180'),)), ('MUTTON BIRAYANI', (('250', '250'),)), ('CHICKEN FRIEDRICE', (('160 ', '160'),)), ('PIZZA', (('240', '240'),)), ('CHICKEN PIZZA', (('280', '280'),)), ('VEG PIZZA', (('210', '210'),)), ('BURGER', (('120', '120'),))], default=None, max_length=100),
        ),
    ]
