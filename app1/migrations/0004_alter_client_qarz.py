# Generated by Django 4.1.5 on 2023-02-21 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_alter_mahsulot_brend'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='qarz',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
    ]
