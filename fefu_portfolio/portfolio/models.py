from django.db import models

from users.models import User


class TypesOfAchievements(models.Model):
    TRP_SIGN = 'Знак отличия ВФСК ГТО'
    VICTORY_OR_PRIZE_PLACE = 'Победа/призовое место в спортивном мероприятии'
    SUPPORT = 'Сопровождение одного из направлений мероприятия ДВФУ(техническая группа, ведущие, фото-/видео- съемка)'
    SPORT_CATEGORY_OR_TITLE = 'Спортивный разряд/звание'
    JUDGING_EVENT = 'Судейство мероприятия'

    TYPES_OF_ACHIEVEMENTS = [
        (TRP_SIGN, TRP_SIGN),
        (VICTORY_OR_PRIZE_PLACE, VICTORY_OR_PRIZE_PLACE),
        (SUPPORT, SUPPORT),
        (SPORT_CATEGORY_OR_TITLE, SPORT_CATEGORY_OR_TITLE),
        (JUDGING_EVENT, JUDGING_EVENT)
    ]

    type_of_achievement = models.CharField(
        max_length=255,
        choices=TYPES_OF_ACHIEVEMENTS,
        verbose_name='Тип достижения',
    )

    class Meta:
        verbose_name = 'Типы достижений'
        verbose_name_plural = 'Типы достижений'

    def __str__(self):
        return self.type_of_achievement


class TRPsigns(models.Model):
    GOLD_SIGN = 'Золотой'
    SILVER_SIGN = 'Серебряный'
    BRONZE_SIGN = 'Бронзовый'

    TYPES_OF_SIGNS = [
        (GOLD_SIGN, GOLD_SIGN),
        (SILVER_SIGN, SILVER_SIGN),
        (BRONZE_SIGN, BRONZE_SIGN)
    ]

    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Студент'
    )
    type_of_sign = models.CharField(
        max_length=255,
        choices=TYPES_OF_SIGNS,
        verbose_name='Вид знака',
    )
    name_of_sign = models.CharField(
        max_length=255,
        verbose_name='Название знака отличия ВФСК'
    )
    unique_number = models.CharField(
        max_length=255,
        unique=True,
        verbose_name='Уникальный идентификационный номер'
    )
    number_of_certificate = models.CharField(
        max_length=255,
        verbose_name='Номер удостоверения о награждении знаком отличия ВФСК ГТО'
    )
    date = models.DateField(
        verbose_name='Дата приказа о награждении'
    )
    type_of_achievement = models.OneToOneField(
        TypesOfAchievements,
        on_delete=models.CASCADE,
        null=True,
        verbose_name='Тип достижения'
    )

    class Meta:
        verbose_name = 'Знаки отличия ВФСК ГТО'
        verbose_name_plural = 'Знаки отличия ВФСК ГТО'

    def __str__(self):
        return f'{self.student}, {self.type_of_sign}'










