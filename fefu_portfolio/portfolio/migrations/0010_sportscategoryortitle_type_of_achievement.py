# Generated by Django 5.0 on 2023-12-19 17:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0009_sportscategoryortitle'),
    ]

    operations = [
        migrations.AddField(
            model_name='sportscategoryortitle',
            name='type_of_achievement',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='portfolio.typesofachievements', verbose_name='Тип достижения'),
        ),
    ]