# Generated by Django 3.2 on 2022-03-22 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0003_auto_20220323_0144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_patient',
            name='idnational',
            field=models.IntegerField(default=''),
        ),
    ]