# Generated by Django 4.0.3 on 2022-03-22 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_purchase_cgst_amount_purchase_igst_amount_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1024)),
                ('email', models.CharField(max_length=1024)),
                ('subject', models.CharField(max_length=1024)),
                ('message', models.CharField(max_length=1024)),
            ],
        ),
        migrations.DeleteModel(
            name='Purchase',
        ),
    ]