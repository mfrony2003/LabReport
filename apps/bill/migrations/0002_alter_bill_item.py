# Generated by Django 5.0.2 on 2024-03-06 03:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bill', '0001_initial'),
        ('diagnosis', '0003_diagnosis_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='item',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='diagnosis.diagnosis'),
        ),
    ]
