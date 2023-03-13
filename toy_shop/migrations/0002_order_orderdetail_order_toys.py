# Generated by Django 4.1.3 on 2023-02-21 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('toy_shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('name', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('all_price', models.FloatField(max_length=30, verbose_name='Общая цена')),
                ('order_uuid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='toy_shop.order')),
                ('toy_uuid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='toy_shop.toy')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='toys',
            field=models.ManyToManyField(through='toy_shop.OrderDetail', to='toy_shop.toy'),
        ),
    ]