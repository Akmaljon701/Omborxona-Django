# Generated by Django 4.1.5 on 2023-02-20 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_mahsulot_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mahsulot',
            name='brend',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
