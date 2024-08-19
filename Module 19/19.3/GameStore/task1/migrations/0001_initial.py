# Generated by Django 5.1 on 2024-08-19 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('balance', models.DecimalField(decimal_places=2, max_digits=10)),
                ('age', models.DecimalField(decimal_places=0, max_digits=3)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('size', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.CharField(max_length=256)),
                ('age_limited', models.BooleanField(default=False)),
                ('buyer', models.ManyToManyField(to='task1.buyer')),
            ],
        ),
    ]
