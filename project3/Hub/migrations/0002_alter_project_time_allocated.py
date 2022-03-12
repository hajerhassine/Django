# Generated by Django 3.2 on 2022-02-07 15:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hub', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='time_allocated',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1, 'the minimum Value required is 1'), django.core.validators.MaxValueValidator(10, 'the maximum Value required is 10')], verbose_name='temps alloue'),
        ),
    ]
