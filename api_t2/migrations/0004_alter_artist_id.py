# Generated by Django 3.2 on 2021-04-21 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_t2', '0003_auto_20210421_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='id',
            field=models.CharField(editable=False, max_length=22, primary_key=True, serialize=False, unique=True),
        ),
    ]
