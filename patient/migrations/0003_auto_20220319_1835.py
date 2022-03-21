# Generated by Django 3.2 on 2022-03-19 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0002_auto_20220319_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_patient',
            name='diagnosis',
            field=models.TextField(blank=True, max_length=1200, null=True, verbose_name='Diagnosis'),
        ),
        migrations.AlterField(
            model_name='add_patient',
            name='note',
            field=models.TextField(blank=True, max_length=1200, null=True, verbose_name='Dr. Notes'),
        ),
        migrations.AlterField(
            model_name='add_patient',
            name='treatment',
            field=models.TextField(blank=True, max_length=1200, null=True, verbose_name='Treatment'),
        ),
    ]
