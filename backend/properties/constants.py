from django.db.models import TextChoices


class QuartersChoices(TextChoices):
    FIRST_QUARTER = "I", "I"
    SECOND_QUARTER = "II", "II"
    THIRD_QUARTER = "III", "III"
    FOURTH_QUARTER = "IV", "IV"


class RoomsCountChoices(TextChoices):
    STUDIO = "Studio", "Студия"
    ONE_ROOM = "One room", "1-а комн."
    TWO_ROOM = "Two room", "2-х комн."
    THREE_ROOM = "Three room", "3-х комн."
    FOUR_ROOM = "Four room", "4-х комн."
    FIVE_ROOM = "Five room", "5-ти комн."
    SIX_ROOM = "Six room", "6-ти комн."


class StatusChoices(TextChoices):
    SOLD = "Sold", "Продана"
    FREE = "Free", "Свободна"
