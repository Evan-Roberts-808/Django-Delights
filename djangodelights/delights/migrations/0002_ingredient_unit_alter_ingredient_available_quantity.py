# Generated by Django 4.2.7 on 2023-11-25 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delights', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='unit',
            field=models.CharField(default='N/A', max_length=50),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='available_quantity',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
