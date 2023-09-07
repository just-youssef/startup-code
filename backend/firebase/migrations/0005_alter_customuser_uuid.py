# Generated by Django 4.1 on 2023-08-13 16:59

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('firebase', '0004_alter_customuser_date_joined'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='uuid',
            field=models.TextField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='UUID'),
        ),
    ]
