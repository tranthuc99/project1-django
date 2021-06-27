# Generated by Django 3.2.4 on 2021-06-21 01:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('cate_id', models.AutoField(primary_key=True, serialize=False)),
                ('cate_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('prod_id', models.AutoField(primary_key=True, serialize=False)),
                ('prod_name', models.CharField(max_length=100)),
                ('prod_price', models.DecimalField(decimal_places=3, max_digits=6)),
                ('prod_description', models.TextField()),
                ('prod_imgage', models.CharField(max_length=30)),
                ('prod_status', models.BooleanField(default=True)),
                ('cate_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.category')),
            ],
        ),
    ]
