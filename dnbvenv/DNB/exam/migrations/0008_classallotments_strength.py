# Generated by Django 4.1.4 on 2023-09-13 07:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0001_initial'),
        ('exam', '0007_remove_classallotments_strength'),
    ]

    operations = [
        migrations.AddField(
            model_name='classallotments',
            name='strength',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='classroom.classes'),
        ),
    ]
