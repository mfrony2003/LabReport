# Generated by Django 5.0.2 on 2024-03-12 02:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bill', '0002_alter_bill_item'),
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bill',
            name='deliverydate',
        ),
        migrations.RemoveField(
            model_name='bill',
            name='deliverytime',
        ),
        migrations.RemoveField(
            model_name='bill',
            name='item',
        ),
        migrations.RemoveField(
            model_name='bill',
            name='user',
        ),
        migrations.AddField(
            model_name='bill',
            name='myPatientReport',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='patient.mypatientreport'),
        ),
        migrations.AddField(
            model_name='bill',
            name='status',
            field=models.CharField(choices=[('Paid', 'Paid'), ('Pending', 'Pending')], default='Pending', max_length=10),
        ),
        migrations.AddField(
            model_name='bill',
            name='totalAmount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
