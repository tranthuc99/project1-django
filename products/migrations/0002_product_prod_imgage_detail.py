# Generated by Django 3.2.4 on 2021-06-21 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='prod_imgage_detail',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
