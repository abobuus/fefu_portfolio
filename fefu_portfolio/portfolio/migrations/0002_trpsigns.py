# Generated by Django 5.0 on 2023-12-19 14:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TRPsigns',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_sign', models.CharField(choices=[('Золотой', 'Золотой'), ('Серебряный', 'Серебряный'), ('Бронзовый', 'Бронзовый')], max_length=255, verbose_name='Вид знака')),
                ('name_of_sign', models.CharField(max_length=255)),
                ('unique_number', models.CharField(max_length=255, unique=True)),
                ('number_of_certificate', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('type_of_achievement', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='portfolio.typesofachievements')),
            ],
            options={
                'verbose_name': 'Знаки отличия ВФСК ГТО',
                'verbose_name_plural': 'Знаки отличия ВФСК ГТО',
            },
        ),
    ]
