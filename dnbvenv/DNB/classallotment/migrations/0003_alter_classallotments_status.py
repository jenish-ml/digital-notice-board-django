# Generated by Django 4.1.4 on 2023-09-01 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classallotment', '0002_classallotments_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classallotments',
            name='status',
            field=models.CharField(default='0', max_length=100),
        ),
    ]
