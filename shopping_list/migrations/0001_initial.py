# Generated by Django 3.0.12 on 2021-06-16 07:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Larder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_in_stock', models.IntegerField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopping_list.Item')),
            ],
        ),
        migrations.CreateModel(
            name='ShoppingTrip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visited_on', models.DateField(auto_now=True)),
                ('money_spent', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=30)),
                ('larder_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopping_list.Larder')),
            ],
        ),
        migrations.CreateModel(
            name='ShoppingAuditEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity_bought', models.IntegerField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopping_list.Item')),
                ('shopping_trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopping_list.ShoppingTrip')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopping_list.User')),
            ],
        ),
    ]
