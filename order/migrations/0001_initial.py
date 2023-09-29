# Generated by Django 4.2.5 on 2023-09-26 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('items', models.JSONField()),
            ],
        ),
    ]
