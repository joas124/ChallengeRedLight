# Generated by Django 4.2.1 on 2023-05-25 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interships', '0004_alter_intern_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rolestatus',
            name='status',
            field=models.CharField(choices=[('Rejected', 'Rejected'), ('Under analysis', 'Under analysis'), ('Approved', 'Approved')], default='Under analysis', max_length=14),
        ),
    ]
