# Generated by Django 2.2.11 on 2020-09-24 17:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('interviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionresult',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
