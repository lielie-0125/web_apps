# Generated by Django 3.0.2 on 2020-02-20 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('permit', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='areainfo',
            name='identifier',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]