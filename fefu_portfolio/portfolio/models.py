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


class VictoryOrPrizePlaces(models.Model):
    INCLUDE = True
    EXCLUDE = False

    EVENT_INCLUDE = [
        (INCLUDE, 'Да'),
        (EXCLUDE, 'Нет')
    ]

    IN_FEFU_TEAM = True
    NOT_IN_FEFU_TEAM = False

    FEFU_TEAM = [
        (IN_FEFU_TEAM, 'Да'),
        (NOT_IN_FEFU_TEAM, 'Нет')
    ]

    PLACE_FIRST = 1
    PLACE_SECOND = 2
    PLACE_THIRD = 3

    PLACE = [
        (PLACE_FIRST, PLACE_FIRST),
        (PLACE_SECOND, PLACE_SECOND),
        (PLACE_THIRD, PLACE_THIRD)
    ]

    STATUS_INTRA_UNIVERSITY = 'Внутривузовский'
    STATUS_REGIONAL = 'Региональный'
    STATUS_INTERREGIONAL = 'Межрегиональный(ДВФО)'
    STATUS_ALL_RUSSIAN = 'Всеросийский'
    STATUS_INTERNATIONAL = 'Международный'

    STATUS_OF_THE_EVENT = [
        (STATUS_INTRA_UNIVERSITY, STATUS_INTRA_UNIVERSITY),
        (STATUS_REGIONAL, STATUS_REGIONAL),
        (STATUS_INTERREGIONAL, STATUS_INTERREGIONAL),
        (STATUS_ALL_RUSSIAN, STATUS_ALL_RUSSIAN),
        (STATUS_INTERNATIONAL, STATUS_INTERNATIONAL)
    ]

    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Студент'
    )
    event_include = models.BooleanField(
        choices=EVENT_INCLUDE,
        verbose_name='Мероприятие включено в официальные календари организаций, '
                     'занимающихся проведением студенческих соревнований?'
    )
    fefu_team = models.BooleanField(
        choices=FEFU_TEAM,
        verbose_name='Принадлежность к сборной ДВФУ?'
    )
    place = models.IntegerField(
        choices=PLACE,
        verbose_name='Достижение'
    )
    status_of_the_event = models.CharField(
        max_length=255,
        choices=STATUS_OF_THE_EVENT,
        verbose_name='Уровень(статус) мероприятия'
    )
    name = models.CharField(
        max_length=255,
        verbose_name='Название спортивного мероприятия'
    )
    type_of_achievement = models.OneToOneField(
        TypesOfAchievements,
        on_delete=models.CASCADE,
        null=True,
        verbose_name='Тип достижения'
    )

    def __str__(self):
        return f'{self.student}, {self.name}, {self.place} место, {self.status_of_the_event}'

    class Meta:
        verbose_name = 'Победы/призовые места в спортивных мероприятиях'
        verbose_name_plural = 'Победы/призовые места в спортивных мероприятиях'


class SupportsOfDirections(models.Model):
    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Студент'
    )
    link_to_the_event = models.URLField(
        verbose_name='Ссылка на мероприятие(с указанием результата выступления)'
    )
    venue = models.CharField(
        max_length=255,
        verbose_name='Место проведения/площадка'
    )
    conducting_organization = models.CharField(
        max_length=255,
        verbose_name='Проводящая организация'
    )
    date_of_the_event_the_beginning = models.DateField(
        verbose_name='Дата проведения - начало'
    )
    date_of_the_event_the_ending = models.DateField(
        verbose_name='Дата проведения - окончание'
    )
    type_of_achievement = models.OneToOneField(
        TypesOfAchievements,
        on_delete=models.CASCADE,
        null=True,
        verbose_name='Тип достижения'
    )

    def __str__(self):
        return f'{self.student}, {self.link_to_the_event}'

    class Meta:
        verbose_name = 'Сопровождения одного из направлений мероприятия ДВФУ'
        verbose_name_plural = 'Сопровождения одного из направлений мероприятия ДВФУ'


class SportsCategoryOrTitle(models.Model):
    MASTER_OF_SPORTS_OF_INTERNATIONAL_CLASS = 'Мастер спорта международного класса'
    MASTER_OF_SPORTS_OF_RUSSIA = 'Мастер спорта России'
    GRANDMASTER_OF_RUSSIA = 'Гроссмейстер России'
    CANDIDATE_FOR_MASTER_OF_SPORTS = 'Кандидат в мастера спорта'

    NAME_OF_THE_CATEGORIES_OR_TITLES = [
        (MASTER_OF_SPORTS_OF_INTERNATIONAL_CLASS, MASTER_OF_SPORTS_OF_INTERNATIONAL_CLASS),
        (MASTER_OF_SPORTS_OF_RUSSIA, MASTER_OF_SPORTS_OF_RUSSIA),
        (GRANDMASTER_OF_RUSSIA, GRANDMASTER_OF_RUSSIA),
        (CANDIDATE_FOR_MASTER_OF_SPORTS, CANDIDATE_FOR_MASTER_OF_SPORTS)
    ]

    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Студент'
    )
    name_of_the_categories_or_titles = models.CharField(
        max_length=255,
        choices=NAME_OF_THE_CATEGORIES_OR_TITLES,
        verbose_name='Наименование разряда/звания'
    )
    type_of_sport = models.CharField(
        max_length=255,
        verbose_name='Вид спорта'
    )
    date_of_assignment = models.DateField(
        verbose_name='Дата присвоения'
    )
    type_of_achievement = models.OneToOneField(
        TypesOfAchievements,
        on_delete=models.CASCADE,
        null=True,
        verbose_name='Тип достижения'
    )

    def __str__(self):
        return f'{self.student}, {self.type_of_sport} {self.name_of_the_categories_or_titles}'

    class Meta:
        verbose_name = 'Спортивные разряды/звания'
        verbose_name_plural = 'Спортивные разряды/звания'