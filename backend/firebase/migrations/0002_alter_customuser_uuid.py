# Generated by Django 4.1 on 2023-08-13 16:01

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('firebase', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='uuid',
            field=models.TextField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
