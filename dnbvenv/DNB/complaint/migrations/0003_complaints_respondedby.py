# Generated by Django 4.1.4 on 2023-08-30 08:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('complaint', '0002_remove_complaints_respondedby_alter_complaints_uid'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaints',
            name='respondedby',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
