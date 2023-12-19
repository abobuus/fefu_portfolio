# Generated by Django 5.0 on 2023-12-19 14:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_trpsigns'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='trpsigns',
            name='date',
            field=models.DateField(verbose_name='Дата приказа о награждении'),
        ),
        migrations.AlterField(
            model_name='trpsigns',
            name='name_of_sign',
            field=models.CharField(max_length=255, verbose_name='Название знака отличия ВФСК'),
        ),
        migrations.AlterField(
            model_name='trpsigns',
            name='number_of_certificate',
            field=models.CharField(max_length=255, verbose_name='Номер удостоверения о награждении знаком отличия ВФСК ГТО'),
        ),
        migrations.AlterField(
            model_name='trpsigns',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Студент'),
        ),
        migrations.AlterField(
            model_name='trpsigns',
            name='type_of_achievement',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='portfolio.typesofachievements', verbose_name='Тип достижения'),
        ),
        migrations.AlterField(
            model_name='trpsigns',
            name='unique_number',
            field=models.CharField(max_length=255, unique=True, verbose_name='Уникальный идентификационный номер'),
        ),
    ]
