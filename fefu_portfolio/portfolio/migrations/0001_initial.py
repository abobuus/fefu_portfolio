# Generated by Django 5.0 on 2023-12-19 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TypesOfAchievements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_achievement', models.CharField(choices=[('Знак отличия ВФСК ГТО', 'Знак отличия ВФСК ГТО'), ('Победа/призовое место в спортивном мероприятии', 'Победа/призовое место в спортивном мероприятии'), ('Сопровождение одного из направлений мероприятия ДВФУ(техническая группа, ведущие, фото-/видео- съемка)', 'Сопровождение одного из направлений мероприятия ДВФУ(техническая группа, ведущие, фото-/видео- съемка)'), ('Спортивный разряд/звание', 'Спортивный разряд/звание'), ('Судейство мероприятия', 'Судейство мероприятия')], max_length=255, verbose_name='Тип достижения')),
            ],
            options={
                'verbose_name': 'Типы достижений',
                'verbose_name_plural': 'Типы достижений',
            },
        ),
    ]
