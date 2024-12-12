# Generated by Django 5.1.2 on 2024-11-04 16:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('modified_at', models.DateTimeField(auto_now_add=True)),
                ('category_name', models.CharField(max_length=100)),
                ('category_image', models.ImageField(upload_to='categories')),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('modified_at', models.DateTimeField(auto_now_add=True)),
                ('Product_name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('Product_discription', models.TextField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prodcuts', to='products.category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('modified_at', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(upload_to='product')),
                ('Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_images', to='products.product')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]